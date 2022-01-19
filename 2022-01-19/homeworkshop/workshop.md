1. 

```python
# 1. List의 합 구하기

numbers = list(map(int, input().split()))

def list_sum(n):
    Hab = 0
    for i in n:
        Hab += i
    return Hab

print(numbers)
print(list_sum(numbers))
```



2. 

```python
# 2. Dictionary로 이루어진 List의 합 구하기

def dict_list_sum(n):
    Hab = 0
    for i in n:
        Hab += i['age'] # i는 각각의 dictionary
    return Hab

dict_list_sum([{'name': 'kim', 'age' : 12}, {'name': 'lee', 'age' : 4}])
```





3. 

```python
# 3. 2차원 List의 전체 합 구하기

def all_list_sum(n):
    Hab_a = []
    Hab_b = 0
    
    for i in n:
        Hab = 0
        for p in i:
            Hab += p
        Hab_a.append(Hab)#각각의 list의 합을 원소로 갖는 list 생성
            
    for i in Hab_a:
        Hab_b += i

    print(Hab_a)
    return Hab_b   
    

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])
```
