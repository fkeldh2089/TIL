1. MTV

​		MTV는 Model(응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리), Template(파일의 구조나 레이아웃을 정의, 실제 내용을 보여주는 데 사용), View(HTTP의 요청을 수신, 응답을 반환하고 Model을 통해 요청을 충족시키는데 필요한 데이터에 접근하며, template에게 응답의 서식을 맡긴다.)의 약자이다.



2. 404 Page not found

(a) articles 

(b) views

(c) views.articles



3. templates and static

(a) settings.py

(b) TEMPLATES

(c) STATIC_URL



4. migration

(1) `python manage.py makemigrations`

(2) `python manage.py  sqlmigrate articles 0001`

(3) `python manage.py showmigrations`

(4) `python manage.py migrate`



5. ModelForm True or False

(1) F

(2) T

(3) T

(4) T



6. media 파일 경로

`MEDIA_ROOT = BASE_DIR / 'media'`

`MEDIA_URL = '/media/'`



7. DB True or False

(1) T

(2) F

(3) T

(4) T

(5) F



8. on_delete

`CASCADE`