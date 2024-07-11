from django.db import models
from members.models import UserInfo
from django.urls import reverse

# Create your models here.

class Movies(models.Model):
    movie_id = models.PositiveIntegerField(primary_key=True)
    movie_name = models.CharField(max_length=127)
    movie_description = models.TextField()
    movie_image = models.URLField()

    def __str__(self):
        return f"{self.movie_name}"
    
class MovieUserReview(models.Model):
    user_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column="user_id")
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE, db_column="movie_id")
    rating = models.FloatField()
    review = models.TextField()

    def __str__(self):
        return "User"
    