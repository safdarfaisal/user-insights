from django.contrib import admin
from .models import Movies, MovieUserReview

# Register your models here.
admin.site.register(Movies)
admin.site.register(MovieUserReview)