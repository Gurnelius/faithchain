from django.db import models
from django.contrib.auth.models import User

class Bible(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Testament(models.Model):
    NEW_TESTAMENT = 'New'
    OLD_TESTAMENT = 'Old'

    TESTAMENT_CHOICES = [
        (NEW_TESTAMENT, 'New Testament'),
        (OLD_TESTAMENT, 'Old Testament'),
    ]
    
    id = models.BigAutoField(primary_key=True)
    bible_version = models.ForeignKey(Bible, on_delete=models.CASCADE)
    name = models.CharField(max_length=3, choices=TESTAMENT_CHOICES, default=OLD_TESTAMENT)

    def __str__(self):
        return self.get_name_display()

class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    testament = models.ForeignKey(Testament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.id}: {self.name}"

class Chapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return f'{self.book.name} {self.number}'

class Verse(models.Model):
    id = models.BigAutoField(primary_key=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.chapter.book.name} {self.chapter.number}:{self.number}'

# Track user reading

class UserReadingProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    time_spent = models.DurationField(null=True, blank=True)  # New field to track time spent reading

    def __str__(self):
        return f'{self.user.username} - {self.book.name} Chapter {self.chapter.number}'