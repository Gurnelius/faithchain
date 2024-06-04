import os
import re
from bs4 import BeautifulSoup
import django
from django.core.management.base import BaseCommand

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

from bible.models import Testament, Bible, Book, Chapter, Verse

class Command(BaseCommand):
    help = 'Scrape the king_james_bible.html file and store data in the database'

    def handle(self, *args, **kwargs):
        # Define the path to the HTML file
        file_path = 'bible/data/new_king_james_bible.html'

        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Parse the page content
        soup = BeautifulSoup(content, 'html.parser')

        # Assume we have only one Bible version for simplicity
        bible, created = Bible.objects.get_or_create(name="King James Version", abbreviation="KJV")

        # Initialize testament to None
        current_testament = None

        # Parse the page content
        chapters = soup.find_all('div', class_='chapter')

        for chapter in chapters:
            title_tag = chapter.find('h2')
            title_text = title_tag.text.strip()
            chapter_parts = chapter.find_all('p')

            # Check if the title indicates a testament
            if 'Old Testament' in title_text:
                current_testament, created = Testament.objects.get_or_create(name=Testament.OLD_TESTAMENT, bible_version=bible)
                print("Old Testament: ", current_testament)
                continue  # Skip to the next iteration because this is not a chapter

            elif 'New Testament' in title_text:
                current_testament, created = Testament.objects.get_or_create(name=Testament.NEW_TESTAMENT, bible_version=bible)
                print("New Testament: ", current_testament)
                continue  # Skip to the next iteration because this is not a chapter

            # Ensure current_testament is set before proceeding
            if current_testament is None:
                self.stdout.write(self.style.ERROR('Testament is not set. Skipping chapter parsing.'))
                continue

            book_name = title_text.strip()  # Extract book name from title
            chapter_number = None

            # Get or create the book
            book, created = Book.objects.get_or_create(
                testament=current_testament,
                name=book_name,
                abbreviation=book_name[:3]
            )

            # Extract verses
            for verse in chapter_parts:
                verse_text = verse.text.strip()
                chapter_verse_number, verse_content = verse_text.split(' ', 1)
                
                try:
                    pattern = r"\d+:\d+"

                    match = re.search(pattern, chapter_verse_number)

                    chapter_verse_number = chapter_verse_number[match.start():match.end()].split(":")
                    chapter_number, verse_number = int(chapter_verse_number[0]), int(chapter_verse_number[1])
                except ValueError:
                    print(verse_content)

                # Get or create the chapter
                chapter, created = Chapter.objects.get_or_create(
                    book=book,
                    number=chapter_number
                )

                if created:
                    # Create the verse
                    Verse.objects.create(
                        chapter=chapter,
                        number=verse_number,
                        text=verse_content.strip()
                    )

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved Bible data'))
