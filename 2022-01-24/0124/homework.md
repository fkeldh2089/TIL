1. 

```python
# 1. 모음은 몇 개나 있을까?
def count_vowels(n): 
    k = 'aeiou' # 모든 모음을 갖는 문자열 k
    ans = 0 # 변수 설정
    for i in k: # 모음 하나하나에 대하여
        ans += n.count(i) # n이 모음을 갖고 있으면 ans += 1
    return ans
```



2. 

```python
# 2. 문자열 조작
st = 'straberry'
st.find('k')
st.split('r')
st.replace('r', 'o', 2)
st.strip('')
#4번, 특정문자를 지정하지 않아도 오류가 발생하지 않는다. 공백을 제거한다.
```





3. 

```python
# 3. 정사각형만 만들기
def only_square_area(n, m):
    ans = []
    l0 = 0
    #print(l0)
    l1 = 0
    for i in n: # 각 list의 길이
        l0 += 1
    for i in m:
        l1 += 1

    for i in range(0, l0): # 각 리스트가 같은 값을 갖고있으면 곱해서 ans에 추가
        #print(n[i])
        for k in range(0, l1):
            #print(m[k])
            if n[i] == m[k]:
                ans.append(n[i] * m[k])
    tmp = set(ans) # 중복 값 제거
    ans = list(tmp)
    return ans
        
```
