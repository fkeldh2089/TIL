# PJT05

obj : 프레임워크 기반 웹페이지 구현



### 요구사항

게시판 기능 개발을 위한 단계, 프로젝트 이름은 `pjt05` 앱 이름은 `movies`

1. 가상환경 설정 및 `pip install -r requirements.txt`를 통해 환경 설정
2. 프로젝트 생성 `django-admin pjt05 .`, 앱 생성 `python manage.py startapp movies`
3. `runserver`를 통해 확인



### Models

1. 요구 사항에 맞게, 다음과 같이 작성

```python
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()
```

2. `python  manage.py makemigrations`, `python manage.py migrate`를 통해 SQL 모델 설정
3. SQLITE EXPLORER를 통해 생성 된 것을 확인,



### URLS

1. 요구 사항에 맞게 다음과 같이 작성

```python
from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),

]
```

- `movies` 앱 하단에 `urls.py`에 작성, 및 namespace를 고려하여, `app_name` 설정



### Admin

1. `python mange.py createsuperuser`를 통해 admin 계정 생성
   - username : admin, password : admin
2. admin/ 접속하여 확인
3. `movies.admin.py`에 Model 추가 및 가시성 확보를 위한 디스플레이 변환

```python
from django.contrib import admin
from .models import Movie

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'audience', 'release_date')

admin.site.register(Movie, MovieAdmin)
```

4. admin 페이지에서 적당한 영화 추가를 통해 동작을 확인,



### View, Templates

##### Base.html

1. 앱과 같은 경로에 `Base.html` 생성, `pjt05.setting.py`에서 경로 추가

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
  <div class="container" style="height: 3000px;">
    {% block content %}
    {% endblock %}
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```



##### Index(메인 페이지)

모든 영화를 조회하는 페이지

1. views.index

```python
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/index.html', context)
```

2. index.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>INDEX</h1>
<a href="#">NEW</a><hr>
{% for movie in movies %}
  <a href="#">{{movie.title}}</a><br>
  <p>{{movie.score}}</p>
{% endfor %}
{% endblock content %}
```

- 대략적인 형태만 갖추고, url은 다른 부분을 완성하고 채운다.



##### Detail(상세 페이지)

각 영화의 상세내용 출력

1. views.detail

```python
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }
    return render(request, 'movies/detail.html', context)
```

- 주소로 받는 pk값을 통해 영화를 받고, 그에 대한 내용을 출력하도록 한다.



2. detail.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>DETAIL</h1>
<hr>
<img class="img-fluid" src="{{movie.poster_url}}" alt="">
<p>{{movie.title}}</p>
<p>Audience : {{movie.Audience}}</p>
<p>Release Dates : {{movie.release_date}}</p>
<p>Genre : {{movie.genre}}</p>
<p>Score : {{movie.score}}</p>
<p>{{movie.description}}</p>

<a href="#">EDIT</a>
<a href="#">DELETE</a><br>
<a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}
```

- 상세 내용들을 출력하고, 아직 구현되지 않은 부분들의 경로는 # 처리한다.



##### new/create

새 내용을 입력하고, 데이터 베이스에 저장한다.

1. views.new, create

```python
def new(request):
    return render(request, 'movies/new.html')


def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    print(audience)

    movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()
    return redirect('movies:detail', movie.pk)
```

- 오타를 찾느라 고통 받았다, `detail.html`에서 Audience 오타, view 함수에서  오타,,,



2. new.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>NEW</h1>
<hr>
<form action="{% url 'movies:create' %}" method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" id="title" name="title"><br>
  <label for="audience">AUDIENCE:</label>
  <input type="text" id="audience" name="audience"><br>
  <label for="release_date">RELEASE_DATE:</label>
  <input type="date" id="release_date" name="release_date"><br>
  <label for="genre">GENRE:</label>
  <input list="genres" id="genre" name="genre" />
  <datalist id="genres">
      <option value="스릴러">
      <option value="코미디">
      <option value="드라마">
      <option value="호러">
  </datalist><br>
  <label for="score">SCORE:</label>
  <input type="text" id="score" name="score"><br>
  <label for="=poster_url">POSTER_URL:</label>
  <input type="text" id="poster_url" name="poster_url"><br>
  <label for="description">DESCRIPTION:</label>
  <textarea name="description" id="description" cols="30" rows="10"></textarea><br>
  <input type="submit">
</form>
<hr>
<a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}
```



##### Edit/Update

원래 있던 내용을 수정한다.

1. views.edit, update

```python
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    if len(str(movie.release_date.month))==1:
        mo = "0"+str(movie.release_date.month)
    else:
        mo = str(movie.release_date.month)
    rd = str(movie.release_date.year)+"-"+mo+"-"+str(movie.release_date.day)

    context = {
        'movie': movie,
        'rd': rd,
        
    }
    return render(request, 'movies/edit.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')
    movie.save()
    return redirect('movies:detail', movie.pk)
```

- 위에서 했던 생성과 거의 비슷하기 때문에 힘들지는 않았는데,,, release_date를 처리하는데 시간이 걸렸다.
- release_date가 초기값으로 받기 위해서는 '9'가 아닌 '09'로 받아야한다.



2.  edit.html

```django
{% extends 'base.html' %}

{% block content %}
<h1>EDIT</h1>
<hr>
<form action="{% url 'movies:update' movie.pk%}" method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" id="title" name="title" value="{{movie.title}}"><br>

  <label for="audience">AUDIENCE:</label>
  <input type="text" id="audience" name="audience" value="{{movie.audience}}"><br>

  <label for="release_date">RELEASE_DATE:</label>
  <input type="date" id="release_date" name="release_date" value="{{rd}}"><br>

  <label for="genre">GENRE:</label>
  <input list="genres" id="genre" name="genre" value="{{movie.genre}}"/>
  <datalist id="genres">
      <option value="스릴러">
      <option value="코미디">
      <option value="드라마">
      <option value="호러">
  </datalist><br>
  <label for="score">SCORE:</label>
  <input type="text" id="score" name="score" value="{{movie.score}}"><br>
  <label for="=poster_url">POSTER_URL:</label>
  <input type="text" id="poster_url" name="poster_url" value="{{movie.poster_url}}"><br>
  <label for="description">DESCRIPTION:</label>
  <textarea name="description" id="description" cols="30" rows="10">{{movie.description}}</textarea><br>
  <input type="submit">
</form>
<hr>
<a href="{% url 'movies:index' %}">BACK</a>
{% endblock content %}
```

- new와 거의 비슷하다, 초기값을 넣어주기만 하면 된다. release_date의 경우 적당히 손볼 필요가 있음



##### Delete

삭제

1. view.delete

```python
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
```

해당 영화를 지운다.



### 고찰

1. 구현하는 데 있어서 문제는 큰 문제는 없었다.
2. release_date의 초기값을 받는데 있어 더 좋은 방법이 있을지 찾아봐야 한다.