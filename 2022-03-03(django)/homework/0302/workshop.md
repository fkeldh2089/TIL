![img](.\img\img.png)

1. intro/urls.py

```python
from django.contrib import admin
from django.urls import path
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dinner/<str:name>/<str:people>', views.dinner),
]
```



2. pages/view.py

```python
from django.shortcuts import render


def dinner(request, name, people):
    context = {
        'name': name,
        'people': people,
    }
    return render(request, 'dinner.html', context)
```





3. templates/dinner.html

```html
{% block content %}
<h1>저녁 메뉴</h1>
<h1>저녁 먹을 사람?! {{people}}명</h1>
<h1>어떤 메뉴?! {{name}}</h1>

{% endblock content %}
```

