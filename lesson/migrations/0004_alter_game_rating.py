# Generated by Django 5.0.1 on 2024-01-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_rename_course_name_genre_genre_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
