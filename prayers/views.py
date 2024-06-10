
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models

    
class PrayerCategoryListView(ListView):
    
    model = models.PrayerCategory
    fields = '__all__'
    template_name = 'prayers/prayercategory_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class PrayerCategoryDetailView(DetailView):
    model = models.PrayerCategory
    template_name = 'prayers/prayercategory_detail.html'

class PrayerCategoryCreateView(CreateView):
    model = models.PrayerCategory
    fields = '__all__'
    success_url = reverse_lazy('prayercategory_list')
    template_name = 'prayers/prayercategory_create.html'


class PrayerCategoryUpdateView(UpdateView):
    model = models.PrayerCategory
    fields = '__all__'
    template_name = 'prayers/prayercategory_update.html'
    success_url = reverse_lazy('prayercategory_list')


class PrayerCategoryDeleteView(DeleteView):
    model = models.PrayerCategory
    success_url = reverse_lazy('prayercategory_list')
    template_name = 'prayers/prayercategory_delete.html'
    success_url = reverse_lazy('prayercategory_list')
    
class PrayerRequestListView(ListView):
    model = models.PrayerRequest
    fields = '__all__'
    template_name = 'prayers/prayerrequest_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class PrayerRequestDetailView(DetailView):
    model = models.PrayerRequest
    template_name = 'prayers/prayerrequest_detail.html'

class PrayerRequestCreateView(CreateView):
    model = models.PrayerRequest
    fields = '__all__'
    success_url = reverse_lazy('prayerrequest_list')
    template_name = 'prayers/prayerrequest_create.html'


class PrayerRequestUpdateView(UpdateView):
    model = models.PrayerRequest
    fields = '__all__'
    template_name = 'prayers/prayerrequest_update.html'
    success_url = reverse_lazy('prayerrequest_list')


class PrayerRequestDeleteView(DeleteView):
    model = models.PrayerRequest
    success_url = reverse_lazy('prayerrequest_list')
    template_name = 'prayers/prayerrequest_delete.html'
    success_url = reverse_lazy('prayerrequest_list')
    
class PrayerListView(ListView):
    model = models.Prayer
    fields = '__all__'
    template_name = 'prayers/prayer_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields = self.model._meta.get_fields()
        context['fields_data'] = [
            {field.name: getattr(obj, field.name) for field in fields if not field.is_relation}
            for obj in context['object_list']
        ]
        return context

class PrayerDetailView(DetailView):
    model = models.Prayer
    template_name = 'prayers/prayer_detail.html'

class PrayerCreateView(CreateView):
    model = models.Prayer
    fields = '__all__'
    success_url = reverse_lazy('prayer_list')
    template_name = 'prayers/prayer_create.html'


class PrayerUpdateView(UpdateView):
    model = models.Prayer
    fields = '__all__'
    template_name = 'prayers/prayer_update.html'
    success_url = reverse_lazy('prayer_list')


class PrayerDeleteView(DeleteView):
    model = models.Prayer
    success_url = reverse_lazy('prayer_list')
    template_name = 'prayers/prayer_delete.html'
    success_url = reverse_lazy('prayer_list')
    