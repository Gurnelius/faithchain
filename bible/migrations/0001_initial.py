# Generated by Django 5.0.6 on 2024-06-03 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bible',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.book')),
            ],
        ),
        migrations.CreateModel(
            name='Testament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('New', 'New Testament'), ('Old', 'Old Testament')], default='New', max_length=3)),
                ('bible_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.bible')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='testament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.testament'),
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bible.chapter')),
            ],
        ),
    ]
