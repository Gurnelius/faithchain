
from django.utils import timezone

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, Chapter, Verse, UserReadingProgress


class BibleListView(ListView):
    model = models.Bible
    fields = '__all__'
    template_name = 'bible/bible_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class BibleDetailView(DetailView):
    model = models.Bible
    template_name = 'bible/bible_detail.html'

class BibleCreateView(CreateView):
    model = models.Bible
    fields = '__all__'
    success_url = reverse_lazy('bible_list')
    template_name = 'bible/bible_create.html'


class BibleUpdateView(UpdateView):
    model = models.Bible
    fields = '__all__'
    template_name = 'bible/bible_update.html'
    success_url = reverse_lazy('bible_list')


class BibleDeleteView(DeleteView):
    model = models.Bible
    success_url = reverse_lazy('bible_list')
    template_name = 'bible/bible_delete.html'
    success_url = reverse_lazy('bible_list')
    
class TestamentListView(ListView):
    model = models.Testament
    fields = '__all__'
    template_name = 'bible/testament_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class TestamentDetailView(DetailView):
    model = models.Testament
    template_name = 'bible/testament_detail.html'

class TestamentCreateView(CreateView):
    model = models.Testament
    fields = '__all__'
    success_url = reverse_lazy('testament_list')
    template_name = 'bible/testament_create.html'


class TestamentUpdateView(UpdateView):
    model = models.Testament
    fields = '__all__'
    template_name = 'bible/testament_update.html'
    success_url = reverse_lazy('testament_list')


class TestamentDeleteView(DeleteView):
    model = models.Testament
    success_url = reverse_lazy('testament_list')
    template_name = 'bible/testament_delete.html'
    success_url = reverse_lazy('testament_list')
    
class BookListView(ListView):
    model = models.Book
    fields = '__all__'
    template_name = 'bible/book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class BookDetailView(DetailView):
    model = models.Book
    template_name = 'bible/book_detail.html'

class BookCreateView(CreateView):
    model = models.Book
    fields = '__all__'
    success_url = reverse_lazy('book_list')
    template_name = 'bible/book_create.html'


class BookUpdateView(UpdateView):
    model = models.Book
    fields = '__all__'
    template_name = 'bible/book_update.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('book_list')
    template_name = 'bible/book_delete.html'
    success_url = reverse_lazy('book_list')
    
class ChapterListView(ListView):
    model = models.Chapter
    fields = '__all__'
    template_name = 'bible/chapter_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class ChapterDetailView(DetailView):
    model = models.Chapter
    template_name = 'bible/chapter_detail.html'

class ChapterCreateView(CreateView):
    model = models.Chapter
    fields = '__all__'
    success_url = reverse_lazy('chapter_list')
    template_name = 'bible/chapter_create.html'


class ChapterUpdateView(UpdateView):
    model = models.Chapter
    fields = '__all__'
    template_name = 'bible/chapter_update.html'
    success_url = reverse_lazy('chapter_list')


class ChapterDeleteView(DeleteView):
    model = models.Chapter
    success_url = reverse_lazy('chapter_list')
    template_name = 'bible/chapter_delete.html'
    success_url = reverse_lazy('chapter_list')
    
class VerseListView(ListView):
    model = models.Verse
    fields = '__all__'
    template_name = 'bible/verse_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class VerseDetailView(DetailView):
    model = models.Verse
    template_name = 'bible/verse_detail.html'

class VerseCreateView(CreateView):
    model = models.Verse
    fields = '__all__'
    success_url = reverse_lazy('verse_list')
    template_name = 'bible/verse_create.html'


class VerseUpdateView(UpdateView):
    model = models.Verse
    fields = '__all__'
    template_name = 'bible/verse_update.html'
    success_url = reverse_lazy('verse_list')


class VerseDeleteView(DeleteView):
    model = models.Verse
    success_url = reverse_lazy('verse_list')
    template_name = 'bible/verse_delete.html'
    success_url = reverse_lazy('verse_list')


# Views for user Bible reading progress

@login_required
def read_bible(request, book_id, chapter_number):
    book = get_object_or_404(Book, id=book_id)
    chapter = get_object_or_404(Chapter, book=book, number=chapter_number)
    verses = Verse.objects.filter(chapter=chapter)

    if request.method == "POST":
        verse_id = request.POST.get('verse_id')
        verse = get_object_or_404(Verse, id=verse_id)
        UserReadingProgress.objects.create(user=request.user, book=book, chapter=chapter, verse=verse)

    context = {
        'book': book,
        'chapter': chapter,
        'verses': verses,
    }
    return render(request, 'bible/read_bible.html', context)

@login_required
def user_progress(request):
    progress = UserReadingProgress.objects.filter(user=request.user).order_by('-date_read')
    context = {
        'progress': progress,
    }
    return render(request, 'bible/user_progress.html', context)

def search_bible(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Verse.objects.filter(text__icontains=query)
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'bible/search_results.html', context)



@login_required
def default_bible_view(request):
    genesis = get_object_or_404(Book, id=886)
    return redirect('read_bible', book_id=genesis.id, chapter_number=1)

@login_required
def read_bible(request, book_id=None, chapter_number=None):
    # Check if book_id and chapter_number are provided
    if book_id is None or chapter_number is None:
        # Check the user's last reading progress
        last_progress = UserReadingProgress.objects.filter(user=request.user).order_by('-start_time').first()
        if last_progress:
            book_id = last_progress.book.id
            chapter_number = last_progress.chapter.number
        else:
            # Default to Genesis chapter 1 if no progress is found
            genesis = Book.objects.filter(id=886).first()
            print(genesis)
            if genesis:
                return redirect('read_bible', book_id=genesis.id, chapter_number=1)
            else:
                # Handle the case where Genesis is not found in the database
                return render(request, 'no_content_404.html')

    book = get_object_or_404(Book, id=book_id)
    chapter = get_object_or_404(Chapter, book=book, number=chapter_number)
    verses = Verse.objects.filter(chapter=chapter)
    
    # Navigation logic
    previous_chapter = Chapter.objects.filter(book=book, number=chapter_number-1).first()
    next_chapter = Chapter.objects.filter(book=book, number=chapter_number+1).first()

    # Handle user reading progress
    if request.method == "POST":
        # Retrieve and update the current reading progress if it exists
        progress = UserReadingProgress.objects.filter(user=request.user, book=book).last()
        if progress and progress.chapter == chapter:
            time_spent = timezone.now() - progress.start_time
            progress.time_spent = time_spent
            progress.save()
        else:
            # Start tracking a new chapter reading session
            UserReadingProgress.objects.create(user=request.user, book=book, chapter=chapter)

    context = {
        'book': book,
        'chapter': chapter,
        'verses': verses,
        'previous_chapter': previous_chapter,
        'next_chapter': next_chapter,
    }
    return render(request, 'bible/read_bible.html', context)