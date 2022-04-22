1. (1) F, 이외에도 중개모델을 이용할 수 있다.

   (2) T

   (3) F, related name은 필수는 아니다



2. (a) user

   (b) article.like_users.all



3. (a) user_pk

   (b) followers

   (c) filter

   (d) remove

   (e) add



4. User 모델로 대체하고, 첫번째 migrate가 이루어 지지 않았을 경우 발생하는 에러이다. 각 migrations 폴더에서 파일들을 지우고, DB를 삭제해 초기화 한 후에, `python manage.py makemigrations`와 `python manage.py migrate`를 통해 해결 가능하다.



5. 둘다 같은 name을 갖게 되므로, 하나는 변경해야 한다.