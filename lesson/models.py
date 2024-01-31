from django.db import models

# Create your models here.

class Game(models.Model):
    game_title = models.CharField(max_length = 100)
    genre = models.ManyToManyField("Genre", related_name = 'genres')
    release_year = models.IntegerField()
    rating = models.DecimalField(max_digits = 5, decimal_places = 1)

    def __str__(self):
        return self.game_title

class Genre(models.Model):
    genre_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.genre_name