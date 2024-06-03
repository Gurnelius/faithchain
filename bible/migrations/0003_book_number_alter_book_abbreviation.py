# Generated by Django 5.0.6 on 2024-06-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bible', '0002_book_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='number',
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='abbreviation',
            field=models.CharField(max_length=10),
        ),
    ]
