
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

    
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
    