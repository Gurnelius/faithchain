
from django.urls import path
from . import views


urlpatterns = [
    path('prayercategory/', views.PrayerCategoryListView.as_view(), name='prayercategory_list'),
    path('prayercategory/<int:pk>/', views.PrayerCategoryDetailView.as_view(), name='prayercategory_detail'),
    path('prayercategory/create/', views.PrayerCategoryCreateView.as_view(), name='prayercategory_create'),
    path('prayercategory/<int:pk>/update/', views.PrayerCategoryUpdateView.as_view(), name='prayercategory_update'),
    path('prayercategory/<int:pk>/delete/', views.PrayerCategoryDeleteView.as_view(), name='prayercategory_delete'),
]
    
urlpatterns += [
    path('prayercategory/', views.PrayerCategoryListView.as_view(), name='prayercategory_list'),
    path('prayercategory/<int:pk>/', views.PrayerCategoryDetailView.as_view(), name='prayercategory_detail'),
    path('prayercategory/create/', views.PrayerCategoryCreateView.as_view(), name='prayercategory_create'),
    path('prayercategory/<int:pk>/update/', views.PrayerCategoryUpdateView.as_view(), name='prayercategory_update'),
    path('prayercategory/<int:pk>/delete/', views.PrayerCategoryDeleteView.as_view(), name='prayercategory_delete'),
]
    
urlpatterns += [
    path('prayerrequest/', views.PrayerRequestListView.as_view(), name='prayerrequest_list'),
    path('prayerrequest/<int:pk>/', views.PrayerRequestDetailView.as_view(), name='prayerrequest_detail'),
    path('prayerrequest/create/', views.PrayerRequestCreateView.as_view(), name='prayerrequest_create'),
    path('prayerrequest/<int:pk>/update/', views.PrayerRequestUpdateView.as_view(), name='prayerrequest_update'),
    path('prayerrequest/<int:pk>/delete/', views.PrayerRequestDeleteView.as_view(), name='prayerrequest_delete'),
]
    
urlpatterns += [
    path('prayer/', views.PrayerListView.as_view(), name='prayer_list'),
    path('prayer/<int:pk>/', views.PrayerDetailView.as_view(), name='prayer_detail'),
    path('prayer/create/', views.PrayerCreateView.as_view(), name='prayer_create'),
    path('prayer/<int:pk>/update/', views.PrayerUpdateView.as_view(), name='prayer_update'),
    path('prayer/<int:pk>/delete/', views.PrayerDeleteView.as_view(), name='prayer_delete'),
]
    