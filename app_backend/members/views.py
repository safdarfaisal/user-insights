from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.models import User
from .forms import SignUpForm
from views import generic
from app_main.models import WatchHistory

# Create your views here.

class ShowProfilePageView(DetailView):
    model = User

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class WatchHistoryView(DetailView):
    model = WatchHistory
    context_object_name = 'watch_history'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return WatchHistory.objects.filter(user=user).order_by('-watch_date')

    def get_context_data(self, **kwargs):
        context = super(WatchHistoryView, self).get_context_data(**kwargs)
        context['user'] = get_object_or_404(User, username=self.kwargs['username'])
        return context
