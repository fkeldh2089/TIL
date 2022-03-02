# Django Intro



1. 가상환경 시작 및 장고 설치

```python
python -m venv venv  # 생성
source venv/Scripts/activate  # 활성화  
pip install django==3.2.12  # 설치
pip freeze > reqirements  # 환경 텍스트 파일
```



2. 장고 프로젝트 생성

```python
django-admin startproject mypjt .  # 현재 파일에 프로젝트 생성
python manage.py runserver  # 서버 생성 확인
```



3. 앱 등록 후, `setting`에 들어가서 앱을 등록,,(33번 라인)
   - 이 때 `setting`에 먼저 등록하면 안됨,,

```python
python manage.py startapp articles  # articles 라는 앱 생성
```



4. 앱 하위항목의 `view`에 들어가서 함수 작성

```python
from django.shortcuts import render

# Create your views here.
def index(request):  # index 함수 작성
    return render(request, 'index.html')  # 템플릿은 index.html을 불러온다
```



5. 앱의 하단에 `templates`라는 이름의 템플릿 폴더 생성, 폴더 안에 템플릿 생성

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
 <h1>hihi</h1> 
</body>
</html>
```



6.  urls 에서 경로 설정

```python
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```



7. 추가 설정,,(언어 및 시간)

```python
# setting의 맨 마지막
LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'
```





### 문법

1. 변수

```python
{{variable}}  # 로 사용하고,,

def greeting(request):
    foods = {'apple', 'banana', 'coconut',}
    info = {
        'name': 'Alice',  
    }
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'greeting.html', context)

  <h1>안뇽 {{info.name}}</h1>  # 이런 식으로 호출이 된다.
```



2. 필터

```python
{{variable|filter}}
```

```django
<body>
  <h1> 오늘 저녁은 {{pick}}</h1>
  <p>{{pick}}은 {{pick|length}}</p>
  <p>메뉴는 {{foods|join:', '}}</p>
  <a href="/index/">뒤로</a>
</body>
</html>
```



3. 태그

```django
  <ul>
    {% for food in foods %}
    <li>{{food}}</li>
    {% endfor %}
  </ul>

  {#한줄 주석#}
  {% comment "" %}
  싸그리 주석
  {% endcomment %}
```

