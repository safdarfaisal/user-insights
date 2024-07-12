from rest_framework import serializers
from keys.secrets import DEFAULT_FILE_URL
from .models import Movies, MovieUserReview
# Create movie serializer

class MovieSerializer(serializers.ModelSerializer):
    movie_image = serializers.SerializerMethodField()

    class Meta:
        model = Movies
        fields = ['movie_id', 'movie_name', 'movie_description', 'movie_image']

    def get_movie_image(self, obj):
        return obj.movie_image if obj.movie_image else DEFAULT_FILE_URL
    
class MovieReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_id.name', read_only='true')
    movie_name = serializers.CharField(source='movie_id.movie_name', read_only='true')

    class Meta:
        model = MovieUserReview
        fields = ['movie_name', 'user_name', 'rating', 'review']