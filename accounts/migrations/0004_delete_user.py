# Generated by Django 5.0.6 on 2024-06-03 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
