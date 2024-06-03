import os
from bs4 import BeautifulSoup
import django
from django.core.management.base import BaseCommand

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'faith.settings')
django.setup()

from ...models import Testament, Bible, Book, Chapter, Verse

class Command(BaseCommand):
    help = 'Scrape the king_james_bible.html file and store data in the database'

    def handle(self, *args, **kwargs):
        # Define the path to the HTML file
        file_path = 'bible/data/king_james_bible.html'

        # Read the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Parse the page content
        soup = BeautifulSoup(content, 'html.parser')

        # Assume we have only one version for simplicity
        version, created = Bible.objects.get_or_create(name="King James Version", abbreviation="KJV")

        # Initialize testament to None
        current_testament = None

        # Initialize book number to 1
        book_number = 1

        # Parse the page content
        chapters = soup.find_all('div', class_='chapter')

        

        for chapter in chapters:
            title_tag = chapter.find('h2')
            title_text = title_tag.text.strip()
            print(title_text)
            # Check if the title indicates a testament
            if 'Old Testament' in title_text:
                current_testament, created = Testament.objects.get_or_create(name=Testament.OLD_TESTAMENT)
                continue  # Skip to the next iteration because this is not a chapter

            elif 'New Testament' in title_text:
                current_testament, created = Testament.objects.get_or_create(name=Testament.NEW_TESTAMENT)
                continue  # Skip to the next iteration because this is not a chapter
            
            # Process only chapters with verses
            if chapter.find('p'):
                book_name = title_text.split(':')[1].strip()  # Extract book name from title
                chapter_number = None

                # Get or create the book
                book, created = Book.objects.get_or_create(
                    testament=current_testament,
                    name=book_name, 
                    abbreviation=book_name[:3],
                    number = book_number
                )

                # Extract verses
                chapter_parts = chapter.find_all('p')
                for verse in chapter_parts:
                    verse_text = verse.text.strip()
                    chapter_verse_number, verse_content = verse_text.split(' ', 1)
                    chapter_number, verse_number = chapter_verse_number.split(':')
                    
                    # Get or create the chapter
                    chapter_obj, created = Chapter.objects.get_or_create(
                        book=book, 
                        number=int(chapter_number)
                    )

                    # Create the verse
                    Verse.objects.create(
                        chapter=chapter_obj,
                        number=int(verse_number),
                        text=verse_content.strip()
                    )

        self.stdout.write(self.style.SUCCESS('Successfully scraped and saved Bible data'))
