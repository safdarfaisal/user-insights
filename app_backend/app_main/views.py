from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Movies

class MovieDetailView(DetailView):
    model = Movies

    def get_context_data(self, *args, **kwargs):
        mov_menu = Movies.objects.all()
        context = super(Movies, self).get_context_data(*args, **kwargs)
        context["mov_menu"] = mov_menu

        return context
    
class HomeView(ListView):
    model = Movies
    ordering = ['-average_rating']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Movies.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu

        return context
