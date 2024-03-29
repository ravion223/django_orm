# Generated by Django 5.0.1 on 2024-01-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='name',
            new_name='course_name',
        ),
        migrations.RemoveField(
            model_name='game',
            name='genre',
        ),
        migrations.AlterField(
            model_name='game',
            name='release_year',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='game',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='lesson.genre'),
        ),
    ]
