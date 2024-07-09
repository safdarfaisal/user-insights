from django.urls import path
from .views import MovieDetailView, WatchHistoryViewSet

urlpatterns = [
    path('', ),
    path('movie/<int:pk>', MovieDetailView.as_view(), name="movie-detail"),
]
