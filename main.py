import sys
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_orm_lesson.settings")
django.setup()

from lesson.models import Game, Genre

# Game(
#     game_title = "Counter Strike 2",
#     release_year = 2023,
#     rating = 3.5
# ).save()

# game1 = Game.objects.get(id = 1)
# genre1 = Genre.objects.get(id = 2)
# game1.genre.add(genre1)

# game2 = Game.objects.get(id = 2)
# genre2 = Genre.objects.get(id = 3)
# game2.genre.add(genre2)

game3 = Game.objects.get(id = 3)
genre3 = Genre.objects.get(id = 1)
game3.genre.add(genre3)