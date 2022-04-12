1. User model BooleanField

```python
is_staff
is_active
```



2. username max length

- 150

```python
max_length=150
```



3. login validation

```python
 is_staff
```



4. Login 기능 구현

- (a) UserCreationForm
- (b) login
- (c) form.user



5. who are you?

- AnonymousUser



6. 암호화 알고리즘

- PBKDF2



7. Logout 기능 구현

사용자가 정의한 함수 `logout`과 import한 함수 logout이 겹치므로,,

`from django.contrib.auth import logout as auth_logout`

와 같이 둘 중 하나의 이름을 변경해 줄 필요가 있다.

