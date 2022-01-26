1. 

```python
# 1. 무엇이 중복일까
def duplicated_letters(n):
    ans = []
    
    for i in n: # 반복되는 문자가 있으면 ans에 추가
        if n.count(i) > 1:
            ans.append(i)
    ans = list(set(ans)) # 반복되는 경우 제거
    return ans
```



2. 

```python
# 2. 소대소대
def low_and_up(n):
    n0 = n.lower() # 입력되는 문자열 소문자로 초기화
    n1 = n0[::2] # 소문자로 쓸 문자
    n2 = n0[1::2] # 대문자로 쓸 문자
    n2 = n2.upper()
    ans = '' # 리턴할 값
    l1, l2 = 0, 0 # 길이 넣을 변수
    
    for i in n1: # 길이 계산
        l1 += 1
    for i in n2:
        l2 += 1
    
    if l1 == l2: # 만약 길이가 같으면
        for i in range(l1): # 돌아가면서 문자열 더해준다.
            ans += n1[i]
            ans += n2[i]
    else : # 길이가 다르면 
        for i in range(l2): # 돌아가면서 문자열 더해주고
            ans += n1[i]
            ans += n2[i]
        ans = ans + n1[-1] # 마지막 남은 문자 더해준다.
    
    return ans
    
    
```





3. 

```python
# 3. 솔로 천국 만들기
def lonely(n):
    p = 0
    k = 0 # 플래그
    ans = [] # 리턴할 값
    
    while(k == 0): # 반복문
        ans.append(n[p]) # n[p]의 값을 ans에 추가
        n = ''.join(list(map(str, n))) # 문자열로 만들어서
        n = n.lstrip(str(n[p])) # n[p]왼쪽에서 부터 없애버리고
        n = list(n) # 리스트로 만들고
        n =list(map(int, n)) # 다시 구성요소를 int로 변환
        if n == []: # 비게 되면 k = 1 로 반복문 끝
            k = 1
    
    return ans
```
