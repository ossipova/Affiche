from django.db import models


# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=100)

    @property
    def movie_count(self):
        return self.all_movies.all().count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE,
                                 related_name='all_movies')

    @property
    def review_text(self):
        return self.movie_reviews.all()

    def __str__(self):
        return self.title

    @property
    def rating(self):
        count = self.movie_reviews.all().count()
        stars = sum([i.stars for i in self.movie_reviews.all()])
        return stars // count


CHOICES = (
    (1, '*'),
    (2, 2 * '*'),
    (3, 3 * '*'),
    (4, 4 * '*'),
    (5, 5 * '*'),
)


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='movie_reviews')
    stars = models.IntegerField(choices=CHOICES, default=1)

    def __str__(self):
        return self.text
