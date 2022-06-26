from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    fitering_data = models.JSONField(default={
        "movie_query": '',
        "vote_checked": 'release_date', 
        "sort_level": 'down',
        "drama_check": 'on',
        "action_check": 'on',
        'adventure_check': 'on',
        'animation_check': 'on',
        'comedy_check': 'on',
        'crime_check' : 'on',
        'documentary_check': 'on',
        'family_check': 'on',
        'fantasy_check': 'on',
        'hitory_check': 'on',
        'horror_check': 'on',
        'music_check' : 'on',
        'mystery_check': 'on',
        'romance_check': 'on',
        'sf_check': 'on',
        'tv_check': 'on',
        'thriller_check': 'on',
        'war_check': 'on',
        'western_check': 'on',
        })
    movie_count = models.IntegerField(default=0)
    reviewed_data = models.JSONField(default={
        # 장르 번호: [본 갯수, 리뷰 점수, 장르 이름]
        '28': [0, 0, '액션'],
        '12': [0,0, '모험'],
        '16': [0,0,  '애니메이션'],
        '35': [0,0, '코미디'],
        '80': [0, 0, '범죄'],
        '99' : [0, 0, '다큐멘터리'],
        '18': [0, 0, '드라마'],
        '10751': [0, 0, '가족'],
        '14': [0, 0, '판타지'],
        '36': [0, 0, '역사'],
        '27': [0, 0, '드라마'],
        '10402': [0, 0, '음악'],
        '9648': [0, 0, '미스터리'],
        '10749': [0, 0, '로맨스'],
        '878': [0, 0, 'SF'],
        '10770': [0, 0, 'TV 영화'],
        '53': [0, 0, '스릴러'],
        '10752': [0, 0, '전쟁'],
        '37': [0, 0, '서부'],
        })