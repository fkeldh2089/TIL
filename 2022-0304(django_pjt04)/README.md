# pjt04

## 초안

#### 틀 잡기

1. 가상환경 설정
2. gitgnore 생성 (windows, visualstudiocode, python, django)
3. 프로젝트  `pjt04` 생성
4. 앱 `movies` 생성, `setting`에 추가
5. URL mapping을 활용하여, movies에 urls를 이용

```python
# pjt04.urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
]

# movies.urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),  # 이렇게 하면 movie/에서 index를 쓸 수 있나?
    path('recommendations/', views.greeting),
]
```

6. 앱 `movies`하단에 `view`에 함수 생성

```python
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def recommendations(request):
    return render(request, 'recommendations.html')
```

7. 앱 `movies`하단에 `templates`생성 `index.html`과 `recommendations.html`생성

```django

{% block contents %}
<h1>HI</h1>
{% endblock contents %}

{% block contents %}
<h1>Reco</h1>
{% endblock contents %}
```

​		각각 `/movies`경로에 `index.html`가, `/movies/recommendations`에 `recommendations.html`이 나오는 	것을 확인

- `view`에서, `recommendations`에서 TMDB API 요청 및 응답은 틀을 만들고 진행



8. 공유 템플릿 생성

​		(1) `pj04.settings.py`에서 경로를 추가해준다

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

​		(2) `base.html`에 적당한 navbar와 footer를 만든다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>Document</title>
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light fixed top">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  <footer class="fixed-bottom text-center text-align-center" style="height:30px;">
    <p class="mb-0">Web-Django PJT by HJM</p>
  </footer>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```

이 후 명세서에 맞게 적당히 바꿔준다.



### HTML

1. 먼저 `base.html`의 navbar와 footer를 따로 빼서 구현하였다.

```html
<nav class="navbar navbar-expand-lg navbar-light bg-light fixed top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Main</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Recommendations</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<footer class="fixed-bottom text-align-center" style="height:30px;">
  <div class="container">
    <div class="row">
      <p class="col-10 mb-0">Web-bootstrap PJT by HJM</p>
      <a href="#" class="col-1 btn btn-primary btn-lg" role="button">up</a>
    </div>
  </div>
</footer>
```

- navbar는 각각 메인 페이지와 recommendation으로 향하게 해두었다.
- footer의 `up`버튼을 누르면 상단으로 이동한다.



2. main page, `index.html`은 6개의 영화를 조회해야하고, viewport에 따라 레이아웃이 달라진다.

```django
{% extends 'base.html' %}


{% block content %}
<div class="container">
  <section  class="text-center d-flex flex-column justify-content-center">
    <img src="https://via.placeholder.com/840X600.png" alt="main">
  </section>
    
    
  <h1 class="text-center my-5">영화 목록</h1>
  <div class="row">
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <img src="https://via.placeholder.com/600X840.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">쇼생크 탈출</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <img src="https://via.placeholder.com/600X840.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">죽은 시인의 사회</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <img src="https://via.placeholder.com/600X840.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">다크 나이트 라이즈</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <img src="https://via.placeholder.com/600X840.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">그랜드 부다페스트 호텔</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 offset-lg-3 col-lg-3 my-1">
      <div class="card">
        <img src="https://via.placeholder.com/600X840.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">헐</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <img src="https://via.placeholder.com/600X840.png" class="card-img-top" alt="...">
        <div class="card-body">
          <h5 class="card-title">위대한 쇼맨</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
  </div>
</div>
{% endblock content %}
```

- 이 때, section 부분에 텍스트를 집어넣고 싶은데, 진행하면서 바꿔봐야겠다.
- 영화 사진 대신 placeholder를 이용하였다.
- 여기에 Bootstrap Carousel 컴포넌트를 출력할 수 있어야 한다.





### Requests

3. recommendations

- 일단 쇼생크 탈출의 영화 ID를 얻고, 추천 영화에 대한 request를 하여, 추천 영화 목록에서 랜덤으로 하나 뽑았다. 받은 dictionary의 구조를 확인 하고 필요한 부분을 가져가도록 하자.

```python
def recommendations(request):


    def recommendation(title):
        # 1. URL
        base_URL =  'https://api.themoviedb.org/3'
        path_search = '/search/movie'
        #path_recom = '/movie/{movie_id}/recommendations'
        ans = []
        params_search = {  # 영화 찾는 parameter
            'api_key' : '22711168652793b78775bd702f8aaf2c',
            'language' : 'ko',
            'query' : title,
            'region'  : 'KR',
        }
        params_recom = {  # 영화 추천 parameter
            'api_key' : '22711168652793b78775bd702f8aaf2c',
            'language' : 'ko',
        }
        # 2. request
        response_1 = requests.get(base_URL+path_search, params=params_search).json() # search를 request
        k1 = response_1['results']
        for p in k1:
            if p['title'] == title: # 이름이 같은 영화의 id 추출 (쇼생크)
                n = p['id']
                break
        else : # 없으면 None 반환
            return None
        response_2 = requests.get(base_URL+'/movie/' + str(n) + '/recommendations', params=params_recom).json() # recommend request
        k2 = response_2['results'] # 이름과 같은 영화의 제목 리스트에 추가
        for p in k2:
            ans.append(p)


        return ans
    
    movie = random.choice(recommendation('쇼생크 탈출'))
    title = movie['title']
    context = {
        'title': title,
        'movie': movie
    }
    return render(request, 'recommendations.html', context)
```

```
{'adult': False, 'backdrop_path': '/l6hQWH9eDksNJNiXWYRkWqikOdu.jpg', 'genre_ids': [14, 18, 80], 'id': 497, 'media_type': 'movie', 'title': '그린 마일', 'original_language': 'en', 'original_title': 'The Green Mile', 'overview': '미국 루이지애나의 콜드 마운틴 교도소. 폴은 사형수 감방의 간수장으로 일하고 있다. 그의 일은 사형수들을 감독하고, 그린 마일이라 불리는 초록색 복도를 거쳐 그들을 사형 집행장까지 안내하는 것. 폴은 그들이 죽음을 맞이하는 순간까지 평화롭게 지낼 수 있도록 최선을 다한다. 어느 날 존 커피라는 사형수가 이송되어 온다. 그는 쌍둥이 여자아이를 살해한 흉악범. 하지만 순진한 눈망울에 겁을 잔뜩 집어먹은 그의 모습에 폴은 당혹감을 느낀다. 게다가 그는 초자연적 능력으로 폴의 지병을 깨끗하게 치료해주기까지 한다. 존을 전기 의자로 데려가야 할 날이 다가오면서 폴은 그가 무죄라는 확신을 갖게 되는데...', 'popularity': 56.323, 'poster_path': '/yuSpRhrTIJa5JN8oESrfD2bndp1.jpg', 'release_date': '1999-12-10', 'video': False, 'vote_average': 8.5, 'vote_count': 13572}
```

- 'overview', 'poster_path', 'release_date', 'vote_average', 'title'가 필요하다.
  - poster_path의 경우 앞에 `https://image.tmdb.org/t/p/w500/` 가 붙는다.
  - vote_average의 경우 round를 통해 소수 1자리로 반올림 하자

- html 구성,,

```django
{% extends 'base.html' %}

{% block content %}
  <div class="container">
    <head>
      <h2 class="text-center my-5">쇼생크 탈출과 비슷한 영화 추천받기</h2>
    </head>
    <div class="row">
      <section class="col-12 col-md-6 col-lg-3 my-1">
          <img class="img-fluid" src="{{poster_path}}" alt="">
      </section>
      <article class="col-12 col-md-6 col-lg-9 my-1">
        <div class="d-flex flex-row align-items-center ">
          <h4 class="mx-2">{{title}}</h4>
          <button type="button" class="btn btn-primary mx-2">{{vote_average}}</button>
        </div>
        <div class="row">
          <p>{{overview}}</p>
          <small>개봉일 : {{release_date}}</small>
          <a href="#" class="btn btn-primary btn-lg" role="button">상세 정보</a>
        </div>
      </article>
    </div>


  </div>
{% endblock content %}
```

- 근데 상세보기 버튼이랑 TMDB 페이지로 연결 어떻게 하나,,,

  - `https://www.themoviedb.org/movie/` + movie id로 URL 연결
  - 그를 위해 추가로 'id ' 받아오자

  

  

  ### 고찰

  명세서에서 요구하는 기능은 어느정도 구현하였지만, main page에서 부족한 점이 느껴진다.

  1. 영화 포스터를 누르면, 다른 스틸컷이 나오도록 해야하는데, 그렇지 않았다.
  2. 가장 위의 head 부분에, '영화를 추천해 드립니다'라는 텍스트를 집어넣지 않았다.

  부트 스트랩을 써보고 시간이 좀 지나서 그런지, 익숙해지는데 시간이 조금 걸렸다. 또, api를 받고 request하는 것또 과거에 진행했던 프로젝트를 참고하지 않았더라면, 더 많은 시간이 걸릴 뻔 했다.

  

## 수정안

#### index.html

위의 고찰에서 구현하지 못했던, "영화 포스터를 누르면, 다른 스틸컷이 나오도록 해야하는데, 그렇지 않았다."

를 모달을 통해 구현하였다.

```django
{% extends 'base.html' %}


{% block content %}
<div class="container">
  <section  class="text-center d-flex flex-column justify-content-center">
    <img src="https://via.placeholder.com/840X600.png" alt="main">
  </section>
  <h1 class="text-center my-5">영화 목록</h1>
  <div class="row">
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <a href="#" data-bs-toggle="modal" data-bs-target="#movie-1">
          <img src="https://via.placeholder.com/600X840.png" class="img-fluid" alt="">
        </a>
        <div class="card-body">
          <h5 class="card-title">쇼생크 탈출</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <a href="#" data-bs-toggle="modal" data-bs-target="#movie-2">
          <img src="https://via.placeholder.com/600X840.png" class="img-fluid" alt="">
        </a>
        <div class="card-body">
          <h5 class="card-title">죽은 시인의 사회</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <a href="#" data-bs-toggle="modal" data-bs-target="#movie-3">
          <img src="https://via.placeholder.com/600X840.png" class="img-fluid" alt="">
        </a>
        <div class="card-body">
          <h5 class="card-title">다크 나이트 라이즈</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <a href="#" data-bs-toggle="modal" data-bs-target="#movie-4">
          <img src="https://via.placeholder.com/600X840.png" class="img-fluid" alt="">
        </a>
        <div class="card-body">
          <h5 class="card-title">그랜드 부다페스트 호텔</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 offset-lg-3 col-lg-3 my-1">
      <div class="card">
        <a href="#" data-bs-toggle="modal" data-bs-target="#movie-5">
          <img src="https://via.placeholder.com/600X840.png" class="img-fluid" alt="">
        </a>
        <div class="card-body">
          <h5 class="card-title">헐</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
    <article class="col-12 col-sm-6 col-md-4 col-lg-3 my-1">
      <div class="card">
        <a href="#" data-bs-toggle="modal" data-bs-target="#movie-6">
          <img src="https://via.placeholder.com/600X840.png" class="img-fluid" alt="">
        </a>
        <div class="card-body">
          <h5 class="card-title">위대한 쇼맨</h5>
          <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
        </div>
      </div>
    </article>
  </div>

  <div class="modal fade" id="movie-1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div id="carouselExampleIndicators1" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators1" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators1" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators1" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators1" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators1" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="movie-2" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div id="carouselExampleIndicators2" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators2" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="movie-3" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div id="carouselExampleIndicators3" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators3" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators3" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators3" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators3" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators3" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="movie-4" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div id="carouselExampleIndicators4" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators4" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators4" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators4" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators4" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators4" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="movie-5" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div id="carouselExampleIndicators5" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators5" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators5" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators5" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators5" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators5" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  <div class="modal fade" id="movie-6" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
      <div class="modal-content">
        <div id="carouselExampleIndicators6" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators6" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators6" data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators6" data-bs-slide-to="2" aria-label="Slide 3"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
            <div class="carousel-item">
              <img src="https://via.placeholder.com/600X840.png" class="d-block w-100 img-fluid" alt="...">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators6" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators6" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  </div>
  
</div>
{% endblock content %}
```

아직 head 부분의 텍스트를 집어넣지 않았다.



### _nav

base.html의 구성요소를 좀 더 명세서의 사진과 비슷하게 꾸며 보았다.

```django
<nav class="navbar navbar-dark bg-dark fixed-top">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">SSAFY MOVIE</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="/movies/">Main</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/movies/recommendations/">Recommendations</a>
        </li>
      </ul>
    </div>
  </div>
</nav>

<footer class="fixed-bottom p-3 mb-2 bg-secondary text-white" >
  <div class="container">
    <div class="d-flex justify-content-between align-items-center">
      <p class="align-middle my-0">SSAFY</p>
      <a href="#" class="col-1 btn btn-primary btn-lg m-0 img-fluid" role="button">up</a>
    </div>
  </div>
</footer>

```



### 제출후 미흡한 점

1. css 파일을 따로 만들지 않고, html에서 `style`을 사용한 점

2. 배경 이미지를 다루는 법

메인 화면의 배경 이미지를 설정하는 데 있어 시간이 많이 들었고, css파일을 따로 만들지 않고 진행하여 보기 어려운 점도 있다. 만약 유지 보수를 해야하는 코드였다면, 좋지 않은 방식이라 생각된다. 또 코드를 써나감에 있어 많은 반복이 있음을 느꼈지만, 그를 줄일 수 있는 방법이 딱히 떠오르지 않았다는 점도 개선점 중 하나가 될 것이다.
