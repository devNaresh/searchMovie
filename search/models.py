from __future__ import unicode_literals

from django.db import models
# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Movie(models.Model):
    director = models.ForeignKey(Director)
    genre = models.ManyToManyField(Genre)
    popularity = models.FloatField()
    name = models.CharField(max_length=250)
    imdb_score = models.FloatField()

    def __str__(self):
        return self.name
