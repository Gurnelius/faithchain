
from django.contrib import admin
from . import models

admin.site.register(models.Bible)
admin.site.register(models.Testament)
admin.site.register(models.Book)
admin.site.register(models.Chapter)
admin.site.register(models.Verse)