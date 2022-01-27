1. 

```python
# 1. Circle instance 만들기
class Circle:
    pi = 3.14
    
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    
    def area(self):
        return Circle.pi * self.r * self.r
    
    def circumstance(self):
        return 2 * Circle.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
c1 = Circle(3, 2, 4)
print(c1.area())
print(c1.circumstance())
```



2. 

```python
# 2. Dog와 Bird는 Animal 이다.
class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
        
        
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        
    def bark(self):
        print(f'{self.name}! 짖는다!')

    
class Bird(Animal):
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')
        
dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```





3. 

```python
# 3. 오류의 종류
# ZeroDIvisionError : 말 그대로 숫자를 0으로 나눈 경우 발생하는 오류
# NameError : namespace 상에 이름이 없는 경우
# TypeError : 지원하지 않는 타입일 경우
# IndexError : 인덱스가 범위를 벗어나거나 존재하지 않는 경우
# KeyError : 해당 키가 없는 경우
# ModulNotFounError : 존재하지 않는 모듈을 임포트 한 경우
# ImportError : 모듈은 있지만, 존재하지 않는 클래스나 함수를 가져오는 경우
```
