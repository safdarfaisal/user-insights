from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Movies(models.Model):
    movie_name = models.CharField(max_length=255)
    genre = models.CharField(max_length=50)
    average_rating = models.FloatField()
    main_actor1 = models.CharField(max_length=255)
    main_actor2 = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    year = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return f"{self.movie_name} ({self.year}) - {self.average_rating}⭐"
    
    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
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