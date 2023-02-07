# Class magic method

1. `__gt__`, `__len__`

```python
class Person:
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __gt__(self, other):
        print(f'{self.name}: {self.age}살 / {other.name}: {other.age}살')
        return self.age > other.age
    
    def __len__(self):
        return self.height
```

2.`__str__`

```python
class Person:
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def __str__(self):
        return f'<{self.name}> : {self.age}살'
    
    def __gt__(self, other):
        print(f'{self.name}: {self.age}살 / {other.name}: {other.age}살')
        return self.age > other.age
    
    def __len__(self):
        return self.height
```

3. `dir(instance)`
   - 어떤 method를 갖고 있는지 확인

