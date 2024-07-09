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