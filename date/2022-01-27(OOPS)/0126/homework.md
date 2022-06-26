1. 

```python
# 1. Type Class
print(type(int))
print(type(map))
print(type(str))
print(type(float))
print(type(bool))
# int, map, str, float, bool
```



2. 

```python
# 2. Magic Method
# __init__ : 생성자 메소드로 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
# __del__ : 소멸자 메소드로 객체가 파괴되기 직전에 호출되는 메소드
# __str__ : 해당 객체의 출력 형태를 지정, 어떤 인스턴스를 출력하면 return값이 출력
# __repr__ : 문자열을 반환
```





3. 

```python
# 3. Instance method
# L.sort(...) : 리스트 정렬
# L.index(x, start, end) : 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스 반환
# L.append(x) : 리스트 마지막 항목 x 추가
```



4. 

```python
# 4. Module Import
def fibo_recursion(n):
    if n <2:
        return n
    else:
        return fibo_recursion(n - 1) + fibo_recursion(n - 2)

# (a) fibo
# (b) fibo_recursion
# (c) recursion

```

