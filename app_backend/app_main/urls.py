from django.urls import path
from .views import MovieListAPIView, FullReviewListAPIView, MovieReviewListAPIView
urlpatterns = [
    path('', MovieListAPIView.as_view(), name="movielist"), # List view
    path('reviews/', FullReviewListAPIView.as_view() ,name='reviewlist'), # Full Review List
    path('reviews/<int:movie_id>/', MovieReviewListAPIView.as_view(), name='movie_review'), #Specific Movie
]
