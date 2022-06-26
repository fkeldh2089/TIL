from dataclasses import field
from encodings import search_function
from rest_framework import serializers

from movies.models import Movie
from .models import User
from community.models import MovieReview


class UserNameSerializer(serializers.ModelSerializer):

    class UserMovieReviewListSerializer(serializers.ModelSerializer):
        
        class MovieInfoSerializer(serializers.ModelSerializer):

            class Meta:
                model = Movie
                fields = ('id','poster_path')
        movie = MovieInfoSerializer(data='movie', read_only=True)
        class Meta:
            model = MovieReview
            fields = '__all__'
            read_only_fields = ('movie', 'user')
    moviereview_set = UserMovieReviewListSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'