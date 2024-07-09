from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"

class Movie(models.Model):
    movie_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    average_rating = models.FloatField()
    main_actor1 = models.CharField(max_length=255)
    main_actor2 = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return (f"Movie Name: {self.movie_name}, "
                f"Genre: {self.genre}, "
                f"Average Rating: {self.average_rating}, "
                f"Main Actor 1: {self.main_actor1}, "
                f"Main Actor 2: {self.main_actor2}, "
                f"Director: {self.director}, "
                f"Year: {self.year}, "
                f"Review: {self.review}")

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watch_date = models.DateField()
    rating = models.FloatField()
    review = models.TextField()

    def __str__(self):
        return (f"Username: {self.user.username}, "
                f"Watch Date: {self.watch_date}"
                f"Rating: {self.rating}"
                f"Movie: {self.movie.movie_name}"
                f"Genre: {self.movie.genre}, "
                f"Average Rating: {self.movie.average_rating}, "
                f"Main Actor 1: {self.movie.main_actor1}, "
                f"Main Actor 2: {self.movie.main_actor2}, "
                f"Director: {self.movie.director}, "
                f"Year: {self.movie.year}")