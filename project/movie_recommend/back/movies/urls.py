from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),

    # path('recommended/<int:movie_year>/', views.recommended_year, name="recommended_year"),
    path('<int:movie_pk>/moviereview/', views.moviereview_create, name='moviereview_create'),

    # 유경훈
    # 메인알고리즘(Carousel)
    path('finalmovie/', views.finalmovie, name='finalmovie'),
    path('firstsetting/', views.firstsetting, name='firstsetting'),

    # 서브알고리즘
    path('yearago/', views.yearago, name='yearago'),
    path('manygenre/', views.manygenre, name='manygenre'),
    path('votegenre/', views.votegenre, name='votegenre'),
    path('eastasia/', views.eastasia, name='eastasia'),
    path('hardtravel/', views.hardtravel, name='hardtravel'),
    path('asiaoceania/', views.asiaoceania, name='asiaoceania'),
]
