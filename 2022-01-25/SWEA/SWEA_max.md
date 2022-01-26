```python
def mp_2(n):
    a0 = list(n[0])
    a0 = list(map(int,list(a0)))
    a1 = int(n[1])
    b = list(map(int,list(a0)))
    b.sort(reverse = True) #b는 목표값
    opp = 0
    p = 0    
    cnt = 0
    to_c = []
    cgd = []
    
    for i in range(len(a0)): # 바뀌어야 할 숫자들
        if a0[i] != b[i]:
            to_c.append(a0[i])
    print(a0)
    print(b)
    print(to_c)
    
    if a0 == b:
        for i in range(a1): # 최대값에서 남은 횟수만큼 가장 작은 단위만 바꿈
            a0[-1], a0[-2] = a0[-2], a0[-1]
            return a0
    
    
    f = 0 # 플래그
    while(opp < a1 and f == 0):
        tmp = []
        
        
        
        if to_c.count(max(to_c)) == 1:
            to_c[0], to_c[to_c.index(max(to_c))] = max(to_c), to_c[0]
            cgd = to_c[::]
            to_c.remove(max(to_c))
            opp += 1
            
            if to_c == sorted(to_c).reverse: # 정렬이 끝났다면
                f = 1
        
        else:
            if (a1 - opp) >= to_c.count(max(to_c))
            tmp = sorted(to_c[0:to_c.count(max(to_c)):1])
            
            
            for i in range(to_c.count(max(to_c))):
                q = 0
                r = 0
                
                to_c[i] = max(to_c)
                while(q == 0):
                    if to_c[-1 -r] = max(to_c):
                        to_c[-1 -r] = tmp[-1 - i]
                        q = 1
                    else:
                        r += 1
    
    return a0
```

본인의 생각상 두 리스트를 비교하여 하나씩 바꿔나가는 것보다는 차이나는 곳을 빼놓고 구하는 것이 더 빠를 것이라 생각했다. 하지만 위의 코드 처럼 하나씩 가장 높은 값을 지워나가며 풀이하는 것은 결과가 나오지 않게 된다. 결과적으로 다음 번에는 max를 기준으로 삼는 것이 아닌 9~1을 기준으로 삼아 돌려야 겠다.