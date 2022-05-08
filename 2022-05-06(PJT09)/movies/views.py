from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe
from .serializers import MovieListSerializer
from .models import Movie, Genre
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from .forms import MovieForm


# Create your views here.
@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    paginator  = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': page_obj,
        'page_obj': page_obj

    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    movie_form = MovieForm()

    
    context={
        'movie': movie,
        'movie_form': movie_form
    }
    return render (request, 'movies/detail.html', context)


def recommended(request):
    if request.method=="GET":
        movies = Movie.objects.filter(vote_count__gte=10000, popularity__gte=50).order_by('-vote_average')[:10]
    elif request.method == "POST":
        movie_year = request.POST.get('movie_year')
        # movie_year = request.GET['movie_year']
        movies = Movie.objects.filter(release_date__year=int(movie_year), vote_count__gte=10000, popularity__gte=50).order_by('-vote_average')[:10]
    context = {
        'movies': movies,
    }
    return render (request, 'movies/recommended.html', context)


# @require_safe
# def recommended_year(request, movie_year):
#     movies = Movie.objects.filter(vote_count__gte=10000, popularity__gte=50).order_by('-vote_average')[:10]
#     # movies = get_list_or_404(Movie).order_by('-vote_averge')[:10]
#     context = {
#         'movies': movies,
#     }
#     return render (request, 'movies/recommended.html', context)
