1. 

```python
# 1. Built-in 함수와 메서드
n = [1, 3, 2, 5, 7, 10, 16]
n1 = sorted(n)
print(n, n1)
k = [1, 3, 2, 5, 7, 10, 16]
k1 = k.sort()
print(k, k1)
"""
output
[1, 3, 2, 5, 7, 10, 16] [1, 2, 3, 5, 7, 10, 16]
[1, 2, 3, 5, 7, 10, 16] None
 위의 코드에서 알 수 있듯이, sorted()의 경우 정렬된 리스트를 반환하고 원본에 변경이 없지만
.sort()의 경우 원본을 변경하고, None 값을 반환한다.
"""
```



2. 

```python
# 2. .extend()와 .append()의 차이
a = ['a', 'b', 'c', 'd']
print(a)
a.append('robot')
print(a)
b = ['a', 'b', 'c', 'd']
print(b)
b.extend('robot')
print(b)
c = ['a', 'b', 'c', 'd']
print(c)
c.extend(['robot'])
print(c)
"""
output
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'robot']
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'r', 'o', 'b', 'o', 't']
['a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 'robot']
 위의 결과로부터 알 수 있듯이, .append(x)는 x를 추가하고,
.extend(iterable)은 iterable의 항목을 추가한다. 
"""
```





3. 

```python
# 3. 복사가 잘 된건가?
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5

print(a)
print(b)

print(id(a) == id(b))
"""
output
[1, 2, 5, 4, 5]
[1, 2, 5, 4, 5]
True
 결과를 보았을 때, a[2]를 변경한 것이 b[2]에도 영향을 끼쳐 서로 요소가 같은 것을 볼 수 있다.
 그 이유는 id를 비교하였을 때 결과가 True가 나온 것으로 설명할 수 있다.
 이는 a와 b가 서로 같은 리스트를 참조하고 있음을 알 수 있다.
"""
```
