from django.db import models
from musician.models import musicians
from datetime import date
# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=200)
    release_date = models.DateField(default=date.today)
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.IntegerField(choices=RATING_CHOICES)
    musicians = models.ForeignKey(
        musicians, on_delete=models.CASCADE, related_name='album')

    def __str__(self):
        return self.name
