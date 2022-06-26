from dataclasses import field
from encodings import search_function
from rest_framework import serializers
from .models import Movie, Genre
from community.models import MovieReview
from accounts.serializers import UserNameSerializer

class MovieListSerializer(serializers.ModelSerializer):
    
    class GenresSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)

    genres = GenresSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'


class GradingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = '__all__'
        read_only_fields = ('user', 'movie',)


class MovieDetailSerializer(serializers.ModelSerializer):

    class MovieReviewSerializer(serializers.ModelSerializer):
        
        user = UserNameSerializer(data='user', read_only=True)
        class Meta:
            model = MovieReview
            fields = '__all__'
            read_only_fields = ('movie',)

    class GenresSerializer(serializers.ModelSerializer):

        class Meta:
            model = Genre
            fields = ('name',)

    genres = GenresSerializer(many=True, read_only=True)
    moviereview_set = MovieReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

