from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Movies(models.Model):
    movieId = models.PositiveIntegerField(primary_key=True)
    movieName = models.CharField()
    movieDescription = models.TextField()
    movieImage = models.URLField()

    def __str__(self):
        return f"{self.movie_name}"
    

class MovieUserReview(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    movieId = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()

    def __str__(self):
        return "User"