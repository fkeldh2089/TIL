1. 

```python
# 1. 숫자의 의미

def get_secret_word(n):
    asc = []
    ans = str()
    
    for i in n:
        asc.append(chr(i))
    
    for i in asc:
        ans += i
        
    return ans

print(get_secret_word([83, 115, 65, 102, 89]))
```



2. 

```python
# 2. 내 이름은 몇일까?

def get_secret_number(n):
    asc = []
    ans = 0
    
    for i in n:
        asc.append(ord(i))
    
    for i in asc:
        ans += i
    
    return ans

print(get_secret_number('tom'))
    
```





3. 

```python
# 3. 강한 이름

def get_strong_word(a, b):
    asc_1 = []
    asc_2 = []
    ans_1 = 0
    ans_2 = 0
    
    for i in a:
        asc_1.append(ord(i))
        
    for i in b:
        asc_2.append(ord(i))
    
    for i in asc_1:
        ans_1 += i
    
    for i in asc_2:
        ans_2 += i
        
    if ans_1 >= ans_2:
        return a
    else:
        return b
    
print(get_strong_word('z','a'))
print(get_strong_word('tom','john'))
```
