# Django URL



#### URL

​		`path('hello/<str:name>/', views.hello),` 와 같이 구현 가능 <>부분이 변수로 작동

```python
def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)
```

위와 같이 view에서 URL의 변수 부분을 받는 것이 가능

```django
{% extends 'base.html' %}

{% block content %}
<h1>{{name}} 안뇽</h1>
{% endblock content %}
```



#### App URL mapping

​		사용하는 path가 많아질 수 록, 관리가 어려워짐.

- 각 앱에 urls.py를 만들어줌

```python
from django.contrib import admin
from django.urls import path
from articles import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('dtl-practice/', views.dtl_practice),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]

# 프로젝트 폴더에서는 위와 같았던 코드를
# 아래와 같이 변경하여 각각의 app 안에 넣어준다.

from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('dinner/', views.dinner),
    path('dtl-practice/', views.dtl_practice),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]
```

- 이 때 요청이 들어올 때, 프로젝트의 URL에 먼저 접근하므로, 앱의 URL에 연결을 시켜야 한다.

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),  # articles 라는 앱의, url에 연결
]  # 주소가 변경이된다,,
```



#### URL naming

​		url의 주소가 바뀔경우, 관리가 힘들어짐,, 그에 따라

```django
path('index/', views.index, name='index')  

<a href="{% url 'index' %}">뒤로</a>
```

​	위와 같이 `name=''`을 이용하여 표현해 준다.