from django.urls import path
from .views import UserRegisterView, ShowProfilePageView, WatchHistoryView, UserLoginView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show-profile'),
    path('<int:pk>/analytics/', WatchHistoryView.as_view(), name='watch-history'),
    path('login/', UserLoginView.as_view(), name='login'),
]