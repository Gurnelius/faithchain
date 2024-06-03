from django.contrib.auth.models import User
from django.db import models

class PrayerCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class PrayerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Prayer(models.Model):
    prayer_request = models.ForeignKey(PrayerRequest, on_delete=models.CASCADE)
    category = models.ForeignKey(PrayerCategory, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Return the first 50 characters of the prayer content
