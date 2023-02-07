# Class 이터레이터 동작

1. iter 객체를 next를 통해 생성

```python
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```python
rev = Reverse('spam')
iter(rev)
"""
<__main__.Reverse object at 0x00A1DB50>
"""
for char in rev:
    print(char)
"""
m
a
p
s
"""
```

2. 간단하게 yield 를 사용

```python
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
for char in reverse('golf'):
    print(char)
"""
f
l
o
g
"""
```

