from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserInfo(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, db_column="user_id")
    name = models.CharField(max_length=127)
    email = models.EmailField(max_length=254)
    age = models.PositiveSmallIntegerField()
    class Gender(models.TextChoices):
        MALE = 'Male', 'Male'
        FEMALE = 'Female', 'Female'
        NONBINARY = 'Nonbinary', 'Nonbinary'
    gender = models.CharField(max_length=10, choices=Gender.choices)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name}, {self.email}, {self.age}, {self.gender}, {self.date_of_birth}"
    
