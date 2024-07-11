from django.urls import path
from .views import MovieListAPIView
urlpatterns = [
    path('', MovieListAPIView.as_view(), name="movielist"), # List view
]
