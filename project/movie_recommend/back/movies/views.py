from turtle import isvisible
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .serializers import GradingSerializer, MovieListSerializer, MovieDetailSerializer
from .models import Movie, Genre
from community.models import MovieReview
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.paginator import Paginator
from .forms import MovieForm, MovieReviewForm
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .serializers import UserNameSerializer

from movies import serializers
from django.contrib.auth import get_user_model
import json
import random
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.db.models import Sum, Count, Avg


# Create your views here.
# @login_required
@api_view(['GET', 'POST'])
def index(request):
    if request.method=="GET":
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == "POST":  # 필터링 기능 구현
        # print(request.data)
        
        movie_query = request.data.get('moviequery')
        actor_query = request.data.get('actorquery')
        vote_checked = request.data.get('checking')
        sort_level = request.data.get('sort_level')

        drama_check = request.data.get('drama_check')
        action_check = request.data.get('action_check')
        adventure_check = request.data.get('adventure_check')
        animation_check = request.data.get('animation_check')
        comedy_check = request.data.get('comedy_check')
        crime_check = request.data.get('crime_check')
        documentary_check = request.data.get('documentary_check')
        family_check = request.data.get('family_check')
        fantasy_check = request.data.get('fantasy_check')
        hitory_check = request.data.get('hitory_check')
        horror_check = request.data.get('horror_check')
        music_check = request.data.get('music_check')
        mystery_check = request.data.get('mystery_check')
        romance_check = request.data.get('romance_check')
        sf_check = request.data.get('sf_check')
        tv_check = request.data.get('tv_check')
        thriller_check = request.data.get('thriller_check')
        war_check = request.data.get('war_check')
        western_check = request.data.get('western_check')

        runtime = request.data.get('runtime')
        vote_num = request.data.get('vote_num')

        me = User.objects.get(pk=request.user.pk)
        me.fitering_data['movie_query'] = movie_query 

        movies = Movie.objects.annotate(moviereview_num=Count('moviereview'), moviereview_grade=Avg('moviereview__grade') if Count('moviereview') else 0)

        movies = movies.filter(title__icontains=movie_query) # 검색어
        movies = movies.filter(actors__icontains=actor_query)

        filtering_word = ''  # 내림차순, 오름차순 구현
        if sort_level == 'to-up':
            me.fitering_data['sort_level'] = 'up'
        elif sort_level == 'to-down':
            me.fitering_data['sort_level'] = 'down'
        if me.fitering_data['sort_level'] == 'down':
            filtering_word+='-'

        if vote_checked == 'to-vote':  # 날자순, 대중성순, 점수순
            me.fitering_data['vote_checked'] = 'vote_average'
        elif vote_checked == 'to-popu':
            me.fitering_data['vote_checked'] = 'popularity'
        elif vote_checked == 'to-recently':
            me.fitering_data['vote_checked'] = 'release_date'
        elif vote_checked == 'to-reviewnum':
            me.fitering_data['vote_checked'] = 'moviereview_num'
        elif vote_checked == 'to-reviewgrade':
            me.fitering_data['vote_checked'] = 'moviereview_grade'
        

        vote_checked = me.fitering_data['vote_checked']
        sort_level = me.fitering_data['sort_level']


        if drama_check == 'to-off':  # 드라마 18
            movies=movies.filter(genres=18)
        elif drama_check == 'to-on':
            pass

        if action_check == 'to-off':  # 액션 28
            movies=movies.filter(genres=28)
        elif action_check == 'to-on':
            pass

        if adventure_check == 'to-off':  # 어드벤쳐 12
            movies=movies.filter(genres=12)
        elif adventure_check == 'to-on':
            pass

        if animation_check == 'to-off':  # 애니메이션 16
            movies=movies.filter(genres=16)
        elif animation_check == 'to-on':
            pass

        if comedy_check == 'to-off':  # 코미디 35
            movies=movies.filter(genres=35)
        elif comedy_check == 'to-on':
            pass

        if crime_check == 'to-off':  # 범죄 80
            movies=movies.filter(genres=80)
        elif crime_check == 'to-on':
            pass

        if documentary_check == 'to-off':  # 다큐 99
            movies=movies.filter(genres=99)
        elif documentary_check == 'to-on':
            pass

        if family_check == 'to-off':  # 가족 10751
            movies=movies.filter(genres=10751)
        elif family_check == 'to-on':
            pass

        if fantasy_check == 'to-off':  # 판타지 14
            movies=movies.filter(genres=14)
        elif fantasy_check == 'to-on':
            pass

        if hitory_check == 'to-off':  # 역사 36
            movies=movies.filter(genres=36)
        elif hitory_check == 'to-on':
            pass

        if horror_check == 'to-off':  # 호러 27
            movies=movies.filter(genres=27)
        elif horror_check == 'to-on':
            pass

        if music_check == 'to-off':  # 음악 10402
            movies=movies.filter(genres=10402)
        elif action_check == 'to-on':
            pass

        if mystery_check == 'to-off':  # 미스터리 9648
            movies=movies.filter(genres=9648)
        elif mystery_check == 'to-on':
            pass

        if romance_check == 'to-off':  # 로맨스 10749
            movies=movies.filter(genres=10749)
        elif romance_check == 'to-on':
            pass

        if sf_check == 'to-off':  # SF 878
            movies=movies.filter(genres=878)
        elif sf_check == 'to-on':
            pass

        if tv_check == 'to-off':  # 테레비 10770
            movies=movies.filter(genres=10770)
        elif tv_check == 'to-on':
            pass

        if thriller_check == 'to-off':  # 스릴러 53
            movies=movies.filter(genres=53)
        elif thriller_check == 'to-on':
            pass

        if war_check == 'to-off':  # 전쟁 10752
            movies=movies.filter(genres=10752)
        elif war_check == 'to-on':
            pass

        if western_check == 'to-off':  # 서부 37
            me.fitering_data['western_check'] = 'off'
        elif western_check == 'to-on':
            me.fitering_data['western_check'] = 'on'
        if me.fitering_data['western_check'] == 'off':
            movies=movies.filter(genres=37)

        movies = movies.filter(runtime__gte=runtime)  # 러닝 타임
        movies = movies.filter(vote_average__gte=vote_num)  # 평점

        me.save()  # 새로 고침 시 필터 조건 초기화 방지를 위해 유저에 저장


        movies = movies.order_by(filtering_word+vote_checked)
        movies = list(movies)
        print(len(movies))
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def detail(request, movie_pk):
    movie = Movie.objects.annotate(moviereview_num=Count('moviereview'), moviereview_grade=(Sum('moviereview__grade'))).get(pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    sending_detail_data = serializer.data
    num1 = movie.moviereview_num if movie.moviereview_num else 0
    num2 = round(movie.moviereview_grade/movie.moviereview_num, 1) if movie.moviereview_grade and movie.moviereview_num else 0
    sending_detail_data.update({'moviereview_num':num1,'moviereview_grade': num2})
    return Response(sending_detail_data)


@api_view(['POST', 'DELETE'])
def moviereview_create(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        me = User.objects.get(pk=request.user.pk)
        before_write = movie.moviereview_set.filter(user=request.user).first()
    
        if before_write:
            before_grade=before_write.grade
            moviereviewform = MovieReviewForm(request.data, instance=before_write)
            if moviereviewform.is_valid():
                tmp = movie.genres.all()
                # print(before_write.grade)
                for p in range(len(tmp)):
                    me.reviewed_data[str(tmp[p].id)][1] -= before_grade
                review = moviereviewform.save()
                for p in range(len(tmp)):
                    me.reviewed_data[str(tmp[p].id)][1] += int(review.grade)
                me.save()
                return redirect('movies:detail', movie_pk)
        else:
            moviereviewform = MovieReviewForm(request.data)
            if moviereviewform.is_valid():
                review = moviereviewform.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                me.movie_count += 1
                tmp = movie.genres.all()
                for p in range(len(tmp)):
                    me.reviewed_data[str(tmp[p].id)][0] += 1
                for p in range(len(tmp)):
                    me.reviewed_data[str(tmp[p].id)][1] += int(review.grade)
                me.save()
            return redirect('movies:detail', movie_pk)
    else:
        movie = get_object_or_404(Movie, pk=movie_pk)
        me = User.objects.get(pk=request.user.pk)
        review = get_object_or_404(MovieReview,pk=request.data['review_pk'])
        tmp = movie.genres.all()
        me.movie_count -= 1
        for p in range(len(tmp)):
            me.reviewed_data[str(tmp[p].id)][0] -= 1
        for p in range(len(tmp)):
            me.reviewed_data[str(tmp[p].id)][1] -= int(review.grade)
        me.save()
        review.delete()
        return redirect('movies:detail', movie_pk)
        

# 유경훈
@api_view(['GET', 'POST'])
def finalmovie(request):
    country = request.data['country']  # Japan
    if country == 'Australia':
        production_country = 'AU'  # 1 / 8
    elif country == 'Canada':
        production_country = 'CA'  # 3 / 18
    elif country == 'China':
        production_country = 'CN'  # 2 / 11
    elif country == 'France':
        production_country = 'FR'  # 6 / 15
    elif country == 'Germany':
        production_country = 'DE'  # 1 / 11
    elif country == 'Japan':
        production_country = 'JP'  # 27 / 36
    elif country == 'Mexico':
        production_country = 'MX'  # 5 / 10
    elif country == 'Spain':
        production_country = 'ES'  # 6 / 7
    elif country == 'Uk':
        production_country = 'GB'  # 7 / 43
    elif country == 'USA':
        production_country = 'US'  # 190 / 272

    movies = Movie.objects.filter(production_countries__icontains=production_country)
    movies = list(movies)
    random_six_movies = random.sample(movies, 6)    
    serializer = MovieListSerializer(random_six_movies, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def yearago(request):
    today = datetime.now()
    startday1 = today - relativedelta(years=1, months=0, days=3)
    endday3 = today - relativedelta(years=0, months=11, days=28)
    startday1 = startday1.strftime("%Y-%m-%d")  # 2021-05-20 <class 'str'>
    endday3 = endday3.strftime("%Y-%m-%d")  # 2021-05-26 <class 'str'>
    # print(f'시작일, {startday1} ~ 끝일, {endday3}')  # 시작일, 2021-05-20 ~ 끝일, 2021-05-26
    # goal = [startday1, startday2, startday3, startday4, endday1, endday2, endday3]
    movies = Movie.objects.filter(release_date__range=(startday1, endday3))
    movies = list(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def firstsetting(request):
    movies = Movie.objects.filter(popularity__gt=8, vote_average__gt=8)  
    movies = list(movies)
    random_nine_movies = random.sample(movies, 6)
    serializer = MovieListSerializer(random_nine_movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def manygenre(request):
    pk = request.data['data']['pk']  # 사용자 번호
    me = User.objects.get(pk=pk)  # 사용자 object
    serializer = UserNameSerializer(me)
    my_dict = serializer.data['reviewed_data']
    sorted_dict1 = sorted(my_dict.items(), key= lambda x : x[1][1], reverse=True)
    sorted_list1 = sorted_dict1[0:2]  # [('28', [12, 49, '액션']), ('12', [11, 46, '모험'])]
    genre_first = sorted_list1[0][0]  # 28
    movies = Movie.objects.filter(genres=genre_first, popularity__gt=7, vote_average__gt=7)  
    
    # 랜덤개수만큼 랜덤을 돌림으로써, 순서무작위로 들어가도록 함
    movies = list(movies)
    if len(movies) >= 20:
        cnt = 20
    else:
        cnt = len(movies)
    movies = random.sample(movies, cnt)  
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 유경훈
@api_view(['GET', 'POST'])
def votegenre(request):  # 좋게 본 장르 기반 추천 영화
    pk = request.data['data']['pk']  # 사용자 번호
    me = User.objects.get(pk=pk)  # 사용자 object
    serializer = UserNameSerializer(me)
    my_dict2 = serializer.data['reviewed_data']
    sorted_dict2 = sorted(my_dict2.items(), key= lambda x : x[1][1]/x[1][0] if(x[1][0]) else x[1][1], reverse=True)
    sorted_list2 = sorted_dict2[0:2]  # [('10751', [1, 5, '가족']), ('9648', [1, 5, '미스터리'])]
    genre_first = sorted_list2[0][0]  # 10751
    movies = Movie.objects.filter(genres=genre_first, popularity__gt=7, vote_average__gt=7)  
    
    # 랜덤개수만큼 랜덤을 돌림으로써, 순서무작위로 들어가도록 함
    movies = list(movies)
    if len(movies) >= 20:
        cnt = 20
    else:
        cnt = len(movies)
    movies = random.sample(movies, cnt)  
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def eastasia(request):
    movies1 = Movie.objects.filter(production_countries__icontains="KR") # KR 이 들어간 영화
    movies2 = Movie.objects.filter(production_countries__icontains="JP") # JP 이 들어간 영화
    movies3 = Movie.objects.filter(production_countries__icontains="CN") # CN 이 들어간 영화

    movies = movies1.union(movies2, all=False)  # KR + JP 중복불가
    movies = movies.union(movies3, all=False)  # KR + JP + CN 중복불가

    # 랜덤개수만큼 랜덤을 돌림으로써, 순서무작위로 들어가도록 함
    movies = list(movies)
    if len(movies) >= 20:
        cnt = 20
    else:
        cnt = len(movies)
    movies = random.sample(movies, cnt)   

    serializer = MovieListSerializer(movies, many=True)

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def hardtravel(request):
    movies1 = Movie.objects.filter(production_countries__icontains="AE") # AE 이 들어간 영화 1
    movies2 = Movie.objects.filter(production_countries__icontains="AR") # AR 이 들어간 영화 3
    movies3 = Movie.objects.filter(production_countries__icontains="BR") # BR 이 들어간 영화 2
    movies4 = Movie.objects.filter(production_countries__icontains="CL") # CL 이 들어간 영화 1
    movies5 = Movie.objects.filter(production_countries__icontains="CO") # CO 이 들어간 영화 2
    movies6 = Movie.objects.filter(production_countries__icontains="IN") # IN 이 들어간 영화 4
    movies7 = Movie.objects.filter(production_countries__icontains="IS") # IS 이 들어간 영화 1
    movies8 = Movie.objects.filter(production_countries__icontains="MA") # MA 이 들어간 영화 1
    movies9 = Movie.objects.filter(production_countries__icontains="MX") # MX 이 들어간 영화 13
    movies10 = Movie.objects.filter(production_countries__icontains="NO") # NO 이 들어간 영화 1
    movies11 = Movie.objects.filter(production_countries__icontains="NG") # NG 이 들어간 영화 1
    movies12 = Movie.objects.filter(production_countries__icontains="PE") # PE 이 들어간 영화 3
    movies13 = Movie.objects.filter(production_countries__icontains="RO") # RO 이 들어간 영화 1
    movies14 = Movie.objects.filter(production_countries__icontains="VE") # VE 이 들어간 영화 1
    movies15 = Movie.objects.filter(production_countries__icontains="ZA") # ZA 이 들어간 영화 3

    movies = movies1.union(movies2, all=False)  # AE + AR 중복불가
    movies = movies.union(movies3, all=False)   # "  + BR 중복불가
    movies = movies.union(movies4, all=False)   # "  + CL 중복불가
    movies = movies.union(movies5, all=False)   # "  + CO 중복불가
    movies = movies.union(movies6, all=False)   # "  + IN 중복불가
    movies = movies.union(movies7, all=False)   # "  + IS 중복불가
    movies = movies.union(movies8, all=False)   # "  + MA 중복불가
    movies = movies.union(movies9, all=False)   # "  + MX 중복불가
    movies = movies.union(movies10, all=False)  # "  + NO 중복불가
    movies = movies.union(movies11, all=False)  # "  + NG 중복불가
    movies = movies.union(movies12, all=False)  # "  + PE 중복불가
    movies = movies.union(movies13, all=False)  # "  + RO 중복불가
    movies = movies.union(movies14, all=False)  # "  + VE 중복불가
    movies = movies.union(movies15, all=False)  # "  + ZA 중복불가

    # 랜덤개수만큼 랜덤을 돌림으로써, 순서무작위로 들어가도록 함
    movies = list(movies)
    if len(movies) >= 20:
        cnt = 20
    else:
        cnt = len(movies)
    movies = random.sample(movies, cnt)   
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def asiaoceania(request):
    movies1 = Movie.objects.filter(production_countries__icontains="AU") # AU 이 들어간 영화 8
    movies2 = Movie.objects.filter(production_countries__icontains="HK") # HK 이 들어간 영화 2
    movies3 = Movie.objects.filter(production_countries__icontains="NZ") # NZ 이 들어간 영화 2
    movies4 = Movie.objects.filter(production_countries__icontains="TH") # TH 이 들어간 영화 3 
    movies5 = Movie.objects.filter(production_countries__icontains="TW") # TW 이 들어간 영화 1

    movies = movies1.union(movies2, all=False)  # AU + HK 중복불가
    movies = movies.union(movies3, all=False)  # NZ 중복불가
    movies = movies.union(movies4, all=False)  # TH 중복불가
    movies = movies.union(movies5, all=False)  # TW 중복불가

    # 랜덤개수만큼 랜덤을 돌림으로써, 순서무작위로 들어가도록 함
    movies = list(movies)
    if len(movies) >= 20:
        cnt = 20
    else:
        cnt = len(movies)
    movies = random.sample(movies, cnt)   
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
