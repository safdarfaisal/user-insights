from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import LoginView 
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from .forms import SignUpForm
from rest_framework.response import Response
from app_main.models import WatchHistory
from .serializers import LoginSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

class ShowProfilePageView(DetailView):
    model = User

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    

class UserRegisterView(CreateView):
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

class UserLoginView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        print('Hello World')
        serializer = LoginSerializer(data=request.data)
        print('Hello Word')
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print('Hello Words')
                return Response({'message':'Login Successful'}, status=status.HTTP_200_OK, )
            else:
                print('Hello Wordsa')
                return Response({'message':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)