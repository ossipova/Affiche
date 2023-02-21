from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
