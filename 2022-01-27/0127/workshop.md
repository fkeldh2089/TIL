1. 클래스

```python
# 1. 도형 만들기
class Rectangle:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        return (p1.y - p2.y)*(p2.x - p1.x)
    
    def get_perimeter(self):
        return (p1.y - p2.y + p2.x - p1.x) * 2
    
    def sqare(self):
        return (p1.y - p2.y) == (p2.x - p1.x)
    
    
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

```



2.  입력

```python
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.sqare())

p3 = (3, 7)
p4 = (6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.sqare())

```
