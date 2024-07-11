from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from .models import Movies
from .serializers import MovieSerializer

class MovieListAPIView(APIView):
    def get(self, request, format=None):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)