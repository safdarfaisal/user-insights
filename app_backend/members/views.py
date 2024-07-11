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
from .serializers import LoginSerializer
from rest_framework.parsers import JSONParser

# Create your views here.

class UserRegisterView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')


class UserLoginView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return Response({'message':'Login Successful'}, status=status.HTTP_200_OK, )
            else:
                return Response({'message':'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)