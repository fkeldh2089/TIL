1. 

```python
# 1. Built-in 함수
# max(), min(), range(), len(), sum()
```



2. 

```python
# 2. 정중앙 문자

def get_middle_char(m):
    l = 0
    for i in m:
        l += 1
    if l%2:
        return m[l//2:l//2 + 1]
    else:
        return m[l//2 - 1:l//2 + 1]

print(get_middle_char('ssafy'))
print(get_middle_char('coding'))
```





3. 

```python
# 3. 위치 인자와 키워드 인자

def ssafy(name, location = '서울'):
    print(f'{name}의 지역은 {location}입니다')
          
# (1)
ssafy('현준')

# (2)
ssafy(location = '대전', name = '철수')

# (3)
ssafy('영희', location = '광주')

# (4)
#ssafy(name = '길동', '구미')

# (4)번의 경우 키워드 인자 후에 위치 인자를 사용하였기 때문에 오류가 발생한다.
```

4. 

```python
# 4. 나의 반환값은

def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
print(result)
#여기서 result에는 my_func의 반환값이 저장이 될텐데, my_func에는 반환값이 없기 때문에
#None, 즉 아무런 값도 저장되어 있지 않다.
```

5. 

```python
# 5. 가변 인자 리스트

def my_avg(*n):
    Hab = 0
    l = 0
    
    for i in n:
        Hab += i
        l += 1
    return Hab/l

my_avg(77, 83, 95, 80, 70)
```
