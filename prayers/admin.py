
from django.contrib import admin
from . import models

admin.site.register(models.PrayerCategory)
admin.site.register(models.PrayerRequest)
admin.site.register(models.Prayer)