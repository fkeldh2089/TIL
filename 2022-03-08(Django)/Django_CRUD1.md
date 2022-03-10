# SQL



1.  model을 변경할 때, like 설계도

`python manage.py makemigrations`

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
```

		-	다음과 같이 `model`에 설계도를 짜고 명령어를 실행해 준다.

* 주석 처리 한 부분을 나중에 처리한다면,, 빈칸의 기본값들을 처리하는 과정을 겪음
  * app 하단 migration 폴더에 설계도들이 남아있음

2. 마이크레이션을 DB에 반영, 설계도를 DB에 반영 하는 과정

`python manage.py migrate`

-- 깃과 비슷한 느낌이네,,



3. 이 아래는 확인용 코드들

`python manage.py  sqlmigrate articles 0001`



4. 

`python manage.py showmigrations`



# Database API

1. `pip install django_extensions` 설치 및 편의를 위한 `pip install ipython`설치

2. setting에  `'django_extensions',` 앱 추가



1. Create

```python
#1 OOP 처럼,,,
article = Article()  # OOP 처럼,,
article.title = 'first'
article.save()  # 저장

#2 초기 변수 -- django views 함수에서 주로 쓰는 방법
article = Article(title..)
article.save()
#2
Article.objects.create(title.....)  # save까지 포함되어 있는 명령어,,
```



2. Read

```python
#1 
Article.objects.all()
#2 .get
Article.objects.get(title=....)
#3 .filter (field lookups, 참고)
Article.objects.filter(title=....)
```



3. Update

- 조회가 선행되어야 한다. 그 후는 Create와 유사

```python
#1 수정은 조회후, 
article = Article.objects.get(title=....)
....  # 수정 
article.save()  # 저장

#2 삭제
article = Article.objects.get(title=....)
article.delete()  # 삭제, 저장 필요 없음
```

