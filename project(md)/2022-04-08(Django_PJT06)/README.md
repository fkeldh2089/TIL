README

작업 순서대로, 의식의 흐름대로,,

# PJT06

### 프로젝트 및 앱 생성

- 프로젝트 `pjt06` 앱 `movies`생성
- 앱 등록



### model.py 작성

```python
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poseter_url = models.TextField()  # 오타!
    description = models.TextField()

    def __str__(self):
        return self.title
```

- `migrate`



### base.html 작성

- setting.py 에서 경로 설정 후,,



### url 작성

- url 작성 전, 전반적인 동작확인

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index' ),
    
]
```

```python
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'movies/index.html')
```

```django
{% extends 'base.html' %}

{% block content %}
<h1>INDEX</h1>
<a href="#">CREATE</a><hr>
{% for movie in movies %}
  <a href="#">{{movie.title}}</a>
  {{movie.score}}
{% endfor %}
{% endblock content %}
```

- 먼저 기본 틀을 잡기위하여,, 추가적으로 경로 설정을 해둔다.

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index' ),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('new/', views.new, name='new'),
    path('<int:pk>/edit/', views.edit, name='edit')
    
]
```



### Admin

- `python manage.py createsuperuser`로 계정 생성
- admin.py 에 코드

```python
from django.contrib import admin
from .models import Movie

# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'score')

admin.site.register(Movie, MoviesAdmin)
```

- 데이터 추가 및 삭제 가능 여부 확인



### form 작성

- 템플릿을 작성하기 전 편의를 위하여 form 부터 작성한다.

```python
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    gena = 'co'
    genb = 'ho'
    genc = 'ro'
    GENRE_CHOICES=[
        (gena, '코미디'),
        (genb, '호러'),
        (genc, '로맨스'),
    ]
    genre = forms.ChoiceField(widget=forms.Select, choices=GENRE_CHOICES)
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'title',
            }
        )
    )
    Audience = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Audience',
            }
        )
    )
    score = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Score',
            }
        ),
        
        max_value=5, min_value=0
    )

    release_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': '년도-월-일',
            }
        )
    )
        
    class Meta:
        model = Movie
        fields = '__all__'

```

Score의 Step 구현이 안된다,,



### 각각 구현

- #### detail

가장 먼저 detail 구현

```django
{% extends 'base.html' %}

{% block content %}
<h1 class="d-flex justify-content-center">DETAIL</h1>
<hr>
<div class="d-flex justify-content-center">
  <div class="card" style="width: 18rem;">
    <img src="{{movie.poster_url}}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{movie.title}}</h5>
      <p>Audience: {{movie.audience}}</p>
      <p>Realese Dates: {{movie.realese_date}}</p>
      <p>Genre: {{movie.genre}}</p>
      <p>Score: {{movie.score}}</p>
      <p class="card-text">{{movie.description}}</p>
      <a href="#" class="btn btn-primary">UPDATE</a>
      <a href="#" class="btn btn-danger">DELETE</a>
    </div>
  </div>
</div>
<form action="{% url 'movies:index' %}">
  <input type="submit" class="btn btn-warning" value="BACK">
</form>
{% endblock content %}
```

카드를 이용하였고, 이미지는 적당한 것을 끌어다 썼다.



- #### create(new)

먼저 구분하여 만든 다음에,,

```python
def new(request):
    form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)


def create(request):
    form = MovieForm(request.POST)
    movie = form.save()
    return redirect('movies:detail', movie.pk)
```

메소드를 분기로 삼아 하나로 합친다.

```python
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():  # 유효성 검사
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form
    }
    return render(request, 'movies/create.html', context)

```

```django
{% extends 'base.html' %}

{% block content %}
<h1>CREATE</h1><hr>
<form action="{% url 'movies:create' %}"method="POST">
  {% csrf_token %}
  {{form.as_p}}
  <input type="submit" class="btn btn-primary" value="SUBMIT">
</form>
<hr>
<form action="{% url 'movies:index' %}">
  <input type="submit" class="btn btn-info" value="BACK">
</form>
{% endblock content %}
```

디자인은 나중에 하고 넘어 갑시다



- #### update(edit)

```python
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = MovieForm(instance=movie)
    context = {
        'form': form,
        'movie': movie,
    }
    return render(request, 'movies/update.html', context)


def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    form = MovieForm(request.POST, instance=movie)
    movie = form.save()
    return redirect('movies:detail', movie.pk)
```

```python
def update(request, pk):
    movie = Movie.objects.get(pk=pk)
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

```

```django
{% extends 'base.html' %}

{% block content %}
<h1 class="d-flex justify-content-center">DETAIL</h1>
<hr>
<div class="d-flex justify-content-center">
  <div class="card" style="width: 18rem;">
    <img src="{{movie.poster_url}}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{movie.title}}</h5>
      <p>Audience: {{movie.audience}}</p>
      <p>Realese Dates: {{movie.realese_date}}</p>
      <p>Genre: {{movie.genre}}</p>
      <p>Score: {{movie.score}}</p>
      <p class="card-text">{{movie.description}}</p>
      <a href="{% url 'movies:update' movie.pk %}" class="btn btn-primary">UPDATE</a>
      <a href="#" class="btn btn-danger">DELETE</a>
    </div>
  </div>
</div>
<form action="{% url 'movies:index' %}">
  <input type="submit" class="btn btn-warning" value="BACK">
</form>
{% endblock content %}
```



- #### Delete

```python
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:index')
    return redirect('movies:detail', movie.pk)
```

 이 때, a 태그를 통하여 POST로 가져오려고 했는데, a 태그는 POST를 지원하지 않는 듯 하다.



### 마무리

- #### 오류 고치기

  1.  step = 0.5

     - attr 내부에 0.5를 ''로 감싸 작성하였더니 동작하였다

     ```python
         score = forms.IntegerField(
             widget=forms.NumberInput(
                 attrs={
                     'step': '0.5',
                     'placeholder': 'Score',
                 }
             ),
     ```

     

  2. 디자인 수정

     - 기본적인 디자인은 따라가도록 수정하였다
     - [django-bootstrap-v5](https://django-bootstrap-v5.readthedocs.io/en/latest/index.html) 를 이용하여 간단하게 수정하였다.



### 고찰

1. 오타
   - 처음 model을 설정할 때 부터 오타가 있었고, 그로 인하여 혼란이 왔었다,, 주의를 기울여야 할 것 같다
2. 습관
   - 평소대로, 손에 붙은대로 코드를 짜다 보니 movie가 아닌 손에 익은 article이 자꾸 타이핑 되었으며, 구성 요소 또한 전에 사용하던 content를 사용하여, 현재 사용해야 하는 description이 출력되지 않기도 하였다.
3. 기타
   - 그 외에 부트 스트랩 사용법은 복습의 필요성이 있다. 기초적인 부분은 가능하지만, 복잡해지거나, 반응형 웹구성은 기억이 안날지도 모르겠다.

해당 readme에는 오타 및, 오류가 있을 수 있으므로 완성된 코드를 보며 참고하기 바랍니다.