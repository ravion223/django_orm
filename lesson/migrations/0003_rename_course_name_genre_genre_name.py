# Generated by Django 5.0.1 on 2024-01-31 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_rename_name_genre_course_name_remove_game_genre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='course_name',
            new_name='genre_name',
        ),
    ]
