# README

## 작업 흐름

1. 프로젝트 `pjt07` 생성 및 유저 관리 앱 `accounts`생성
2. `accounts.models.py`
   - `AbstractUser` 상속 받는 커스텀 모델 생성
   - `settings.py` 코드 추가

```python
# accounts.models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

# settings.py
AUTH_USER_MODEL = 'accounts.User'  # 추가
```



3. 앱 `movies` 생성

   - 기본적인 CRUD 기능 구현
   - 명세서에 맞게 모델을 먼저 생성,,

   `models.py`

   ```python
   
   class Movie(models.Model):
       title = models.CharField(max_length=20)
       description = models.TextField()
   
       def __str__(self):
           return self.title
   ```

   user_id는 `accounts` 기능을 구현 후 추가 계획
   
   `forms.py`
   
   ```python
   class MovieForm(forms.ModelForm):
   
       class Meta:
           model = Movie
           fields = '__all__'
   ```
   
   `urls.py`
   
   ```python
   from django.urls import path
   from . import views
   
   app_name = 'movies'
   urlpatterns = [
       path('', views.index, name='index'),
       path('<int:pk>/', views.detail, name='detail'),
       path('create/', views.create, name='create'),
       path('<int:pk>/update', views.update, name='update'),
       path('<int:pk>/delete', views.delete, name='delete'),
   ]
   ```
   
   `views.py`
   
   ```python
   from django.shortcuts import render, redirect
   from movies.models import Movie
   from movies.forms import MovieForm
   
   # Create your views here.
   def index(request):
       movies = Movie.objects.order_by('-pk')
       context = {
           'movies': movies
       }
       return render(request, 'movies/index.html', context)
       
   
   def detail(request, pk):
       movie = Movie.objects.get(pk = pk)
       context = {
           'movie': movie,
       }
       return render(request, 'movies/detail.html', context)
   
   
   def create(request):
       if request.method == 'POST':
           form = MovieForm(request.POST)
           if form.is_valid():
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
   ```
   
   - 그 `templates`의 경우, 명세서에 맞게 부트스트랩 없이 구현



4. 앱 `accounts` 기능 추가

   - `login`, `logout`, `signup`,  `delete`, `update`, `change_password`순으로 작업

   `models.py`

   ```python
   from django.db import models
   from django.contrib.auth.models import AbstractUser
   
   # Create your models here.
   class User(AbstractUser):
       pass
   ```

   기존 시작 시 작성 완료

   

   `forms.py`

   ```python
   from django.contrib.auth.forms import UserChangeForm, UserCreationForm
   from django.contrib.auth import get_user_model
   
   from accounts.models import User
   
   
   class CustomUserChangeForm(UserChangeForm):
   
       # password = None
   
       class Meta:
           model = get_user_model() # User
           fields = ('first_name', 'last_name',)
           
   
   class CustomUserCreationForm(UserCreationForm):
   
       class Meta(UserCreationForm.Meta):
           model = get_user_model()
           fields = UserCreationForm.Meta.fields
   ```

   명세서에 따라 first_name과 last_name만 작성할 수 있도록 `CustomUserChangeForm`을 작성하였다.

   

   `urls.py`

   ```python
   from django.urls import path
   from . import views
   
   app_name = 'accounts'
   urlpatterns = [
       path('login/', views.login, name='login'),
       path('logout/', views.logout, name='logout'),
       path('signup/', views.signup, name='signup'),
       path('delete/', views.delete, name='delete'),
       path('update/', views.update, name='update'),
       path('password/', views.change_password, name='change_password'),
   ]
   ```

   

   `views.py`

   ```python
   from django.shortcuts import render, redirect
   from django.contrib.auth import login as auth_login  # 이름이 겹침
   from django.contrib.auth import update_session_auth_hash
   from django.contrib.auth import logout as auth_logout  # 이름이 겹침
   from django.contrib.auth.decorators import login_required
   from django.views.decorators.http import require_http_methods, require_POST
   from django.contrib.auth.forms import (
       AuthenticationForm,
       PasswordChangeForm,
   )
   from .forms import CustomUserChangeForm, CustomUserCreationForm
   
   # Create your views here.
   @require_http_methods(['GET', 'POST'])
   def login(request):
       if request.user.is_authenticated:
           return redirect('movies:index')
   
       if request.method == 'POST':
           form = AuthenticationForm(request, request.POST)
           if form.is_valid():
               auth_login(request, form.get_user())
               return redirect('movies:index')
       else:
           form = AuthenticationForm()
       context = {
           'form': form,
       }
       return render(request, 'accounts/login.html', context)
   
   
   @require_POST
   def logout(request):
       if request.user.is_authenticated:
           auth_logout(request)
       return redirect('movies:index')
   
   
   @require_http_methods(['GET', 'POST'])
   def signup(request):
       if request.user.is_authenticated:
           return redirect('movies:index')
   
       if request.method == 'POST':
           form = CustomUserCreationForm(request.POST)
           if form.is_valid():
               user = form.save()
               auth_login(request, user)
               return redirect('movies:index')
       else:
           form = CustomUserCreationForm()
       context = {
           'form': form,
       }
       return render(request, 'accounts/signup.html', context)
   
   
   @require_POST
   def delete(request):
       if request.user.is_authenticated:
           # 반드시 회원탈퇴 후 로그아웃 함수 호출
           request.user.delete()
           auth_logout(request)
       return redirect('movies:index')
   
   
   @login_required
   @require_http_methods(['GET', 'POST'])
   def update(request):
       if request.method == 'POST':
           form = CustomUserChangeForm(request.POST, instance=request.user)
           if form.is_valid():
               form.save()
               return redirect('movies:index')
       else:
           form = CustomUserChangeForm(instance=request.user)
       context = {
           'form': form,
       }
       return render(request, 'accounts/update.html', context)
   
   
   @login_required
   @require_http_methods(['GET', 'POST'])
   def change_password(request):
       if request.method == 'POST':
           form = PasswordChangeForm(request.user, request.POST)
           if form.is_valid():
               # user = form.save()
               # update_session_auth_hash(request, user)
               form.save()
               update_session_auth_hash(request, form.user)
               return redirect('movies:index')
       else:
           form = PasswordChangeForm(request.user)
       context = {
           'form': form,
       }
       return render(request, 'accounts/change_password.html', context)
   ```

   - 그 `templates`의 경우, 명세서에 맞게 부트스트랩 없이 구현

   

   `base.html`

   ```django
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
     <div class="container">
       {% if request.user.is_authenticated %}
         <h3>Hello, {{ user }}</h3>  
         <a href="{% url 'accounts:update' %}">회원정보수정</a>
         <form action="{% url 'accounts:logout' %}" method="POST">
           {% csrf_token %}
           <input type="submit" value="Logout">
         </form>
         <form action="{% url 'accounts:delete' %}" method="POST">
           {% csrf_token %}
           <input type="submit" value="회원탈퇴">
         </form>
       {% else %}
         <a href="{% url 'accounts:login' %}">Login</a>
         <a href="{% url 'accounts:signup' %}">Signup</a>
         <hr>
       {% endif %}
       {% block content %}
       {% endblock content %}
     </div>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   명세서에 맞게, 로그인 시와, 비로그인 시 화면을 base.html에 구현하였다.

   비로그인 시 `/movies/` 에 Login과 Signup 만을 출력하여, `movies.view.py`에 데코레이터를 쓰지 않고 넘어갔다.



5. `movies`앱에 댓글 기능을 위해  `comment`추가, 및 FK 추가

   - 모델을 구성한 후, 

   `model.py`

   ```python
   from django.db import models
   from django.conf import settings
   
   # Create your models here.
   class Movie(models.Model):
       # user_id를 foreign key로 받음
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
       title = models.CharField(max_length=20)
       description = models.TextField()
   
       def __str__(self):
           return self.title
   
   
   class Comment(models.Model):
       # movie_id, user_id를 foreign key로 받음
       movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
       content = models.CharField(max_length=100)
       user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
       def __str__(self):
           return self.content
   ```



​	`forms.py`

```python
from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        # fields = '__all__'  # user의 경우, views 함수에서 처리합니다.(로그인 유저,,)
        exclude = ('user',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)

```



`url`

```python
from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:movie_pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
]
```



`view`

```python
from django.shortcuts import render, redirect
from movies.models import Movie, Comment
from movies.forms import MovieForm, CommentForm


def detail(request, pk):
    movie = Movie.objects.get(pk = pk)
    comments = movie.comment_set.all()  # 댓글목록 
    comment_form = CommentForm  # 댓글 입력 형식
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
            movie.user = request.user  # FK로 받는 user_id
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm()
    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


def comments_create(request, pk):
    comment_form = CommentForm(request.POST)
    movie = Movie.objects.get(pk=pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.movie = movie  # FK로 받는 movi_id
        comment.user = request.user  # FK로 받는 user_id
        comment.save()
    return redirect('movies:detail', movie.pk)


def comment_delete(request, movie_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('movies:detail', movie_pk)
```

템플릿의 경우, detail 부분만 변경,,



6. `templates`

   - `base.html`

   ```django
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
     <div class="container">
       {% if request.user.is_authenticated %}
         <h3>Hello, {{ user }}</h3>
         <a href="{% url 'accounts:update' %}">회원정보수정</a>
         <form action="{% url 'accounts:logout' %}" method="POST">
           {% csrf_token %}
           <input type="submit" value="Logout">
         </form>
         <form action="{% url 'accounts:delete' %}" method="POST">
           {% csrf_token %}
           <input type="submit" value="회원탈퇴">
         </form>
       {% else %}
         <a href="{% url 'accounts:login' %}">Login</a>
         <a href="{% url 'accounts:signup' %}">Signup</a>
         <hr>
       {% endif %}
       {% block content %}
       {% endblock content %}
     </div>
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

   로그인 시 및 비로그인 상태 구분하여 출력

   - `movie/create.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <hr>
     <h1>CREATE</h1>
     <hr>
     <form action="{% url 'movies:create' %}" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
     </form>
     <hr>
     <a href="{% url 'movies:index' %}">BACK</a>
   {% endblock  %}
   ```

   

   - `movie/detail.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
   <hr>
   <h1>DETAIL</h1>
   <hr>
   <h3>{{ movie.title }}</h3>
   <p>{{ movie.description }}</p>
   <a href="{% url 'movies:update' movie.pk %}">UPDATE</a>
   <form action="{% url 'movies:delete' movie.pk %}" method="POST">
     {% csrf_token %}
     <input type="submit" value="delete">
   </form>
   <a href="{% url 'movies:index' %}">BACK</a>
   <hr>
   <form action="{% url 'movies:comments_create' movie.pk %}" method='POST'>
     {% csrf_token %}
     {{comment_form}}
     <input type="submit">
   </form>
   <hr>
   <h4>댓글</h4>
   <ul>
     {% for comment in comments %}
       <li>
         {{comment.content}}
         {% if  user == comment.user  %}
         <form action="{% url 'movies:comment_delete' movie.pk comment.pk %}" method='POST'>
           {% csrf_token %}
           <input type="submit" value='Delete'>
         </form>
         {% endif %}
       </li>
     {% endfor %}
   </ul>
   {% endblock  %}
   ```

   댓글을 작성한 유저만 해당 댓글을 삭제할 수 있도록, `{% if  user == comment.user  %}`를 사용하였다.

   

   - `movie/index.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>INDEX</h1>
     {% if request.user.is_authenticated %}
       <a href="{% url 'movies:create' %}">CREATE</a>
       <hr>
       {% for movie in movies %}
       <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
         <p></p>
         <hr>
       {% endfor %}
     {% else %}
       
     {% endif %}
   {% endblock  %}
   
   ```

   

   - `movie/update.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <hr>
     <h1>UPDATE</h1>
     <hr>
     <form action="{% url 'movies:update' movie.pk %}" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="reset">
       <input type="submit">
     </form>
     <hr>
     <a href="{% url 'movies:index' %}">BACK</a>
   {% endblock  %}
   ```

   

   - `accounts/login.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>LOGIN</h1>
     <form action="" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
     </form>
     <a href="{% url 'movies:index' %}">back</a>
   {% endblock content %}
   ```

   

   - `accounts/signup.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>Signup</h1>
     <hr>
     <form action="{% url 'accounts:signup' %}" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
     </form>
     <a href="{% url 'movies:index' %}">back</a>
   {% endblock content %}
   
   ```

   

   - `accounts/update.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>회원정보수정</h1>
     <hr>
     <form action="{% url 'accounts:update' %}" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
     </form>
     <a href="{% url 'movies:index' %}">back</a>
   {% endblock content %}
   
   ```

   

   - `accounts/change_password.html`

   ```django
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>비밀번호변경</h1>
     <hr>
     <form action="{% url 'accounts:change_password' %}" method="POST">
       {% csrf_token %}
       {{ form.as_p }}
       <input type="submit">
     </form>
     <a href="{% url 'movies:index' %}">back</a>
   {% endblock content %}
   ```

   



## 고찰

#### 홍제민(navigator)

1.  주로 네비게이터의 역할을 하게 되었는데, 남에게 설명한다는 것이 본인이 직접하는 것보다 더 많은 이해량을 가지고 있어야 하는 것 같다는 생각을 하게되었다.
2. foreign key를 받고, view함수에서 처리하는 데 있어 익숙하지 않아 고생하였다.
3. 막히는 부분에서 같이 찾아보고 고민할 수 있는 팀원이 있다는 것은 큰 도움이 되었다.
4. html에서 python문법이 이리 쉽게 쓸 수 있는지 몰랐다. 특히 댓글을 작성한 본인만이 삭제할 수 있는 기능을 구현할 때, 파이썬에 기반하여 근거없이 작성하였는데, 성공하였다.

#### 최은우(Driver)

처음 드라이버, 네비게이터의 역할을 정하고 1. movies 앱의 CRUD 구문 작성 2. account 앱 3. comment 구문 추가 의 순서로 진행하기로 결정하고 시작하였습니다.  만약 드라이버가 네비게이터보다 아는 것이 많고 진행이 빨랐다면 페어 프로그래밍 하는 과정에서 마찰이나 불협화음이 많이 생겼을 것 같은데 제민님께서 너무 잘 이끌어주시고 수정 사항도 빠르게 안내를 해줘 드라이버로써 크게 어려운 점 없이 코드 작성할 수 있었습니다.
