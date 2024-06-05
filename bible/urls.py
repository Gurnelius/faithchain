
from django.urls import path
from . import views

urlpatterns = [
    path('bible/', views.BibleListView.as_view(), name='bible_list'),
    path('bible/<int:pk>/', views.BibleDetailView.as_view(), name='bible_detail'),
    path('bible/create/', views.BibleCreateView.as_view(), name='bible_create'),
    path('bible/<int:pk>/update/', views.BibleUpdateView.as_view(), name='bible_update'),
    path('bible/<int:pk>/delete/', views.BibleDeleteView.as_view(), name='bible_delete'),
]
    

urlpatterns += [
    path('testament/', views.TestamentListView.as_view(), name='testament_list'),
    path('testament/<int:pk>/', views.TestamentDetailView.as_view(), name='testament_detail'),
    path('testament/create/', views.TestamentCreateView.as_view(), name='testament_create'),
    path('testament/<int:pk>/update/', views.TestamentUpdateView.as_view(), name='testament_update'),
    path('testament/<int:pk>/delete/', views.TestamentDeleteView.as_view(), name='testament_delete'),
]
    
urlpatterns += [
    path('book/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
    
urlpatterns += [
    path('chapter/', views.ChapterListView.as_view(), name='chapter_list'),
    path('chapter/<int:pk>/', views.ChapterDetailView.as_view(), name='chapter_detail'),
    path('chapter/create/', views.ChapterCreateView.as_view(), name='chapter_create'),
    path('chapter/<int:pk>/update/', views.ChapterUpdateView.as_view(), name='chapter_update'),
    path('chapter/<int:pk>/delete/', views.ChapterDeleteView.as_view(), name='chapter_delete'),
]
    
urlpatterns += [
    path('verse/', views.VerseListView.as_view(), name='verse_list'),
    path('verse/<int:pk>/', views.VerseDetailView.as_view(), name='verse_detail'),
    path('verse/create/', views.VerseCreateView.as_view(), name='verse_create'),
    path('verse/<int:pk>/update/', views.VerseUpdateView.as_view(), name='verse_update'),
    path('verse/<int:pk>/delete/', views.VerseDeleteView.as_view(), name='verse_delete'),
]

# Bible Reading Links


urlpatterns = [
    path('read/<int:book_id>/<int:chapter_number>/', views.read_bible, name='read_bible'),
    path('progress/', views.user_progress, name='user_progress'),
    path('search/', views.search_bible, name='search_bible'),
]
