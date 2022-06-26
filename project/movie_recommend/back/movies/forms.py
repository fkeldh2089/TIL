from django import forms
from .models import Movie, Genre
from community.models import MovieReview
# Create your forms here.


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'

class MovieReviewForm(forms.ModelForm):

    class Meta:
        model = MovieReview
        fields = ('grade', 'content',)

