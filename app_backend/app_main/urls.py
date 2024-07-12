from django.urls import path
from .views import MovieListAPIView, FullReviewListAPIView
urlpatterns = [
    path('', MovieListAPIView.as_view(), name="movielist"), # List view
    path('reviews/', FullReviewListAPIView.as_view() ,name='reviewlist'),
]
