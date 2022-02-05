1. 

```python
# 1. pip
"""
faker를 설치하기 위한 명령으로 cmd 나 git bash 등의 프롬프트 창에서 실행하면 된다.
"""
! pip install faker
```



2. 

```python
# 2. Basic usages
# 1. faker에서 Faker를 import 하기 위한 코드
# 2. Faker는 클래스, fake는 인스턴스이다.
# 3. name()은 fake의 instance method이다.
from faker import Faker
fake = Faker()
fake.name()

# output
# 'Matthew Stewart'
```





3. 

```python
# 3. Localization
# (a) init
# (b) self
# (c) n = en_US
```



4. 

```python
# 4-1. Seeding the Generator
import random

random.random()
random.random()

random.seed(7777)
random.random()

random.seed(7777)
random.random()

fake = Faker('ko_KR')
Faker.seed(4321)

print(fake.name())

fake2 = Faker('ko_KR')
print(fake2.name())
# # 1 이도윤
# # 2 이지후
# seed() 는 클래스 메솔드
```

5. 

```python
# 4-2. Seeding the Generator
fake = Faker('ko_KR')
fake.seed_instance(4321)
print(fake.name())

fake2 = Faker('ko_KR')
print(fake2.name())

# # 1 이도윤
# # 2 김광수
# seed_instance()는 인스턴스 메소드로 
# seed() 는 클래스 인자에 접근하여 변경하는 용도
# seed_instance() 는 객체 인스턴스의 상태를 수정하는 용도
```

