# Django_CRUD2

### Delete

```python
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
```

- POST로 받아야 삭제 하도록 한다.



### Update

```python
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```

- 전체적인 구조가 create와 비슷하다. 하지만 html에서, create와 살짝 다른 면이 있다.

```django
{% extends 'base.html' %}

{% block content %}
<h1>Edit</h1>
<hr>
<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <label for="title">Title</label>
  <input type="text" id="title" name="title" value="{{article.title}}">
  <label for="content">Content</label>
  <textarea name="content" id="content" cols="30" rows="10">{{article.content}}</textarea>
  <input type="submit">
</form>

{% endblock content %}
```

- POST로 받는 경우, ` {% csrf_token %}`가 필수적으로 들어간다.
- 이미 작성되어있는 내용을 불러올 필요가 있다.





---

### Admin

`python manage.py createsuperuser`

- 계정 생성

```python
from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)
```

- 디스플레이 변화