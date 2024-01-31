# Generated by Django 5.0.1 on 2024-01-31 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_title', models.CharField(max_length=100)),
                ('release_year', models.IntegerField(max_length=4)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='lesson.genre')),
            ],
        ),
    ]
