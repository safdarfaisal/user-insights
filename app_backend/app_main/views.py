from rest_framework.response import Response
from rest_framework import status
from rest_framework.request import Request 
from rest_framework.views import APIView
from .models import Movies, MovieUserReview
from .serializers import MovieSerializer, MovieReviewSerializer

class MovieListAPIView(APIView):
    def get(self, request, format=None):
        movies = Movies.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FullReviewListAPIView(APIView):
    def get(self, request):
        reviews = MovieUserReview.objects.all()
        serializer = MovieReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class MovieReviewListAPIView(APIView):
    def get(self, request, movie_id):
        movie_review = MovieUserReview.objects.filter(movie_id=movie_id)
        serializer = MovieReviewSerializer(movie_review, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)