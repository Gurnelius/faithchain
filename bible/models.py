from django.db import models


class Bible(models.Model):
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
    
    id = models.BigAutoField(primary_key=True, default=1)
    bible_version = models.ForeignKey(Bible, on_delete=models.CASCADE)
    name = models.CharField(max_length=3, choices=TESTAMENT_CHOICES, default=OLD_TESTAMENT)


    def __str__(self):
        return self.get_name_display()

class Book(models.Model):
    testament = models.ForeignKey(Testament, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    number = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return self.name

class Chapter(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.book.name} {self.number}'

class Verse(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.chapter.book.name} {self.chapter.number}:{self.number}'
