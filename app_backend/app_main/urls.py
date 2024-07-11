from django.urls import path
from .views import MovieDetailView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie/<slug:name>/', MovieDetailView.as_view(), name="movie-detail"),
]
