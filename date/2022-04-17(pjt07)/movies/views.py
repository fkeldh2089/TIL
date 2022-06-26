from django.shortcuts import render, redirect
from movies.models import Movie, Comment
from movies.forms import MovieForm, CommentForm

# Create your views here.
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
    

def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    comments = movie.comment_set.all()
    comment_form = CommentForm
    context = {
        'movie': movie,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)


def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk = pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    movie = Movie.objects.get(pk = pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    else:
        return redirect('movies:detail', movie.pk)


def comments_create(request, pk):
    comment_form = CommentForm(request.POST)
    movie = Movie.objects.get(pk=pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie
        comment.user = request.user
        comment.save()
    return redirect('movies:detail', movie.pk)


def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)