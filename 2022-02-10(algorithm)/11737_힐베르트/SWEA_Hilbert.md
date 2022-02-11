# SWEA_Hilbert

obj : 힐베르트 곡선을 따라 좌표가 존재, 번호를 차례대로 붙이고 주어진 번호 사이의 거리를 구하시오. order는 n, 그리고 a와 b의 거리를 구하면 된다.(input(n, a, b))

![image-20220205135724693](.\img\hil.png)

### 알고리즘 구상

일단 힐베르트 곡선을 만들 필요가 있다. 직접 그려보았는데, 생각보다 어렵다.

1. 재귀를 이용할 필요가 있겠다는 생각이 들었다. 위의 그림에서 b와 c를 이용하여 규칙을 알아볼 필요가 있다.
   - 힐베르트곡선을 만드는 것은 프랙탈이고, 항상 똑같은 규칙이므로 b와 c의 규칙을 전체에 적용할 수 있다.
   - c를 보면 b가 우상단 우하단에 들어가있는 것을 볼 수 있다. 즉(0+2^(3-1)+1, 0)과 (0+2^(3-1)+1, -(2^(3-1)+1))에서 b가 반복되는 것을 알 수 있다.
   - 좌상단과 좌하단은 우상단과 우하단의 대각선으로 대칭, 혹은 90deg 회전 시키면 같다고 볼 수 있다.
2. 좌상단과 좌하단이 문제다.
   - 보아하니, 좌상단은 우상단을 역순으로 짚어가는 것과 같다.
   - 좌하단은 우하단을 역순으로 짚어가는 것과 같다.
3. 집의 번호와 좌표를 엮을 방법이 필요,,





### 좌표 변환1

1. 위의 구상을 토대로 위치와 좌표로 표현하는 재귀 코드를 짜보도록 한다.
2. 가장 중요한 기준점은 

```python
def hilbert_position(n, a):
    if n == 1:
        if a == 1:
            return [0, 0] # 튜플보다는 리스트가 계산하기 편하다.
        elif a == 2:
            return [1, 0]
        elif a == 3:
            return [1, -1]
        elif a == 4:
            return [0, -1]
```

일단 정성적으로 위와 같이 생각한다. 또 힐베르트 곡선의 실제모습과 혼동하지 않기 위하여 좌표평면과 같은 좌표축을 통해 계산하도록 하였다.

3. 재귀를 불러오는 부분은 총 4개로 나누도록 하자.(우상, 좌상, 좌하, 우하)

```python
def hilbert_position(n, a):
    elif n > 1:
        if a <= (2**n): # 우상단
            pass
        elif a <= (2**(n+1)): # 좌상단
            pass
        elif a <= (2**(n+2)): # 좌하단
            pass
        elif a <= (2**(n+3)): # 우하단
            pass
```

좌상단과 우하단의 경우 n-1일 경우과 같은 순서로 움직이므로 쉽게 구현 할 수 있다.

```python
def hilbert_position(n, a):
    elif n > 1:
        offset_H = 0
        new_position = []
        if a <= (2**n): # 좌상단
            pass
        elif a <= (2**(n+1)): # 우상단
            offset_H += 2**(n) 
            new_position = hilbert_position(n-1, a-(2**(n))) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0]+offset_H), new_position[1]]
        elif a <= (2**(n+2)): # 우하단
            offset_H += 2**(n) 
            new_position = hilbert_position(n-1, a-(2**(n+1))) # n-1차 힐베르트 곡선에서 생각
            return [new_position[0]+offset_H, new_position[1]+offset_H]
        elif a <= (2**(n+3)): # 좌하단
            pass
```

일단 여기까지 동작하나 확인



### 좌표변환 2

1. 위 초안 1에서 생각한 코드를 돌려보자 오류가 난다,, 원인으로는

   - 4분할(좌상, 우상, 우하, 좌하)로 나누는 범위가 잘못되었다는 것

   - 그에 따른 동작불능으로 인한 none값 출력

이는 힐베르트 곡선의 좌표의 offset은 직선이고, 차수가 증가할 수 록 2배가 되지만, 집의 개수의 경우는 평면에서의 계산이므로 4배가 된다는 것을 간과하였기 때문이다 이를 바탕으로 다음과 같이 수정

```python
def hilbert_position(n, a):
    if n == 1:
        if a == 1:
            return [0, 0] # 튜플보다는 리스트가 계산하기 편하다.
        elif a == 2:
            return [1, 0]
        elif a == 3:
            return [1, -1]
        elif a == 4:
            return [0, -1]
    elif n > 1:
        offset_H = 0
        each_H = 0
        new_position = []
        if a <= (4**(n - 1)): # 좌상단
            pass
        
        elif a <= (2*4**(n -1)): # 우상단
            offset_H += 2**(n - 1) # 좌표의 경우, n이 1증가시 2배 되므로,,,
            each_H += 4**(n - 1) # 개수의 경우 n이1 증가시 4배가 된다.
            new_position = hilbert_position(n - 1, a - each_H) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0] + offset_H), new_position[1]] # offset만큼 우로 이동해야 같다고 볼 수 있음
        
        elif a <= (3**(n - 1)): # 우하단
            offset_H += 2**(n - 1)
            each_H += 2*4**(n - 1) # 우하단의 경우 우상단의 2배의 집을 지나쳐 옴
            #print(each_H)
            new_position = hilbert_position(n - 1, a - each_H) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0] + offset_H), (new_position[1] - offset_H)]  # 대각선 좌하단으로 이동해야 함
        elif a <= (4**n): # 좌하단
            pass
"""    
input
print(f'#1 {hilbert_position(2, 6)}')
print(f'#2 {hilbert_position(2, 11)}')
print(f'#3 {hilbert_position(3, 22)}')
print(f'#4 {hilbert_position(3, 38)}')


output
#1 [3, 0]
#2 [3, -3]
#3 [7, 0]
#4 [7, -4]
```

위와 같이 좌상단 좌하단의 경우 잘 동작하는 것을 볼 수 있다. 



2. 이제 나머지 좌측에 대한 계산을 짜야한다. 범위는 나눠 졌고, a 번째 집을 n-1차의 몇번째 집으로 대응시켜야 하는지 생각할 필요가 있다.

   - 우상단을 좌하향 대각선으로 대칭시키면 좌상단이 되고,  
   - 우하단을 우상향 대각선으로 대칭시키면 좌하단이 된다.

   이에 따라 적당히 offset을 더해주는 곳을 변경해주면 대략적으로 작동할 듯 하다. 



3. 먼저 좌상단에 대해 생각해보자, n-1차로 끌고 갈때, a에는 변화가 필요가 없다. 하지만 대칭이동이 필요한 점을 생각하면, `y = -x` 에 대하여 대칭이동 시킨 것과 같다. 그러므로, `(x, y)`가 `(-y, -x)`가 된다 생가할 수 있다. 그 점을 이용하도록 하자

```python
    elif n > 1:
        offset_H = 0
        each_H = 0
        new_position = []
        if a <= (4**(n - 1)): # 좌상단
            new_position = hilbert_position(n-1, a)
            return [-new_position[1], -new_position[0]]
```

이 정도이지 않을까 생각이 든다.



4. 좌하단의 경우 n-1차를 우상향 대각선으로 대칭 이동시켰다고 볼수 있다. offset은 `(0, -2^(n-1))`이고 ,, 대칭이동을 어떻게 시키는지를 생각해 볼 필요가 있다.어,,,?

   - 동 n차수의 다른 좌표로 대응시켜 사용한다.
   - 무식하게 대칭이동 시킬 직선을 구해서 계산 하자

   이 두개정도가 떠오른다. 개인적으로 첫번째가 더 쉬워보이니 한 번 만들어보자

   - `a -= 2*4**(n-1)`를 시키고,,, 180deg 회전을 시킨다면 될듯하다.(원점 대칭?)
   - offset은 `(0, -2^(n-1))`일 것이다. 
   - 원점 대칭은 아니고, 좌표를 n차에서 `(2^(n-2) -0.5, 2^(n-2) -0.5)`를 기준으로 대칭 이동 시키면 되겠다.

```python
        elif a <= (4**n): # 좌하단
            tmp_x = 0
            tmp_y = 0
            offset_H = 2**(n - 1)
            each_H += 3*4**(n - 1)
            new_position = hilbert_position(n, a - each_H)
            tmp_x = (2**(n - 2) - 0.5) - new_position[0]
            tmp_y = -(2**(n - 2) - 0.5) - new_position[1]

            return [new_position[0] + 2*tmp_x, new_position[1] + 2*tmp_y - offset_H]
```

이 정도이지 않을까



5. 합쳐 보자

```python
def hilbert_position(n, a):
    if n == 1:
        if a == 1:
            return [0, 0] # 튜플보다는 리스트가 계산하기 편하다.
        elif a == 2:
            return [1, 0]
        elif a == 3:
            return [1, -1]
        elif a == 4:
            return [0, -1]
    elif n > 1:
        offset_H = 0
        each_H = 0
        new_position = []
        if a <= (4**(n - 1)): # 좌상단
            new_position = hilbert_position(n-1, a) #
            return [-new_position[1], -new_position[0]]
            
        
        elif a <= (2*4**(n -1)): # 우상단
            offset_H += 2**(n - 1) # 좌표의 경우, n이 1증가시 2배 되므로,,,
            each_H += 4**(n - 1) # 개수의 경우 n이1 증가시 4배가 된다.
            new_position = hilbert_position(n - 1, a - each_H) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0] + offset_H), new_position[1]] # offset만큼 우로 이동해야 같다고 볼 수 있음
        
        elif a <= (3*4**(n - 1)): # 우하단
            offset_H += 2**(n - 1)
            each_H += 2*4**(n - 1) # 우하단의 경우 우상단의 2배의 집을 지나쳐 옴
            #print(each_H)
            new_position = hilbert_position(n - 1, a - each_H) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0] + offset_H), (new_position[1] - offset_H)]  # 대각선 좌하단으로 이동해야 함
        elif a <= (4**n): # 좌하단
            tmp_x = 0 # 대칭이동 시키기 위한 변수
            tmp_y = 0
            offset_H = 2**(n - 1)
            each_H += 3*4**(n - 1)
            new_position = hilbert_position(n, a - each_H)
            tmp_x = (2**(n - 2) - 0.5) - new_position[0] # 대칭 이동하기 위한 계산
            tmp_y = -(2**(n - 2) - 0.5) - new_position[1]

            return [int(new_position[0] + 2*tmp_x), int(new_position[1] + 2*tmp_y - offset_H)] # 대칭 이동 시키고 offset 더해줌, float형이 되므로 int로 변환
        
"""
input
print(f'#1 {hilbert_position(2, 15)}')
print(f'#2 {hilbert_position(2, 12)}')
print(f'#3 {hilbert_position(3, 54)}')
print(f'#4 {hilbert_position(3, 51)}')

output
#1 [0, -2]
#2 [2, -3]
#3 [3, -4]
#4 [2, -6]
```

결과가 나오는 것을 확인할 수 있다.



### 거리 계산

1. 거리 계산은 간단하다, 위의 함수를 통해 좌표 두개를 구하고 거리를 계산하자

```python
def distant_H(pos1, pos2):
    ans = 0
    ans = ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**(1/2)*10 # 한 칸단 10m
    
    return ans 
```



### 제출용

```python
# 함수부
def hilbert_position(n, a):
    if n == 1:
        if a == 1:
            return [0, 0] # 튜플보다는 리스트가 계산하기 편하다.
        elif a == 2:
            return [1, 0]
        elif a == 3:
            return [1, -1]
        elif a == 4:
            return [0, -1]
    elif n > 1:
        offset_H = 0
        each_H = 0
        new_position = []
        if a <= (4**(n - 1)): # 좌상단
            new_position = hilbert_position(n-1, a) #
            return [-new_position[1], -new_position[0]]
            
        
        elif a <= (2*4**(n -1)): # 우상단
            offset_H += 2**(n - 1) # 좌표의 경우, n이 1증가시 2배 되므로,,,
            each_H += 4**(n - 1) # 개수의 경우 n이1 증가시 4배가 된다.
            new_position = hilbert_position(n - 1, a - each_H) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0] + offset_H), new_position[1]] # offset만큼 우로 이동해야 같다고 볼 수 있음
        
        elif a <= (3*4**(n - 1)): # 우하단
            offset_H += 2**(n - 1)
            each_H += 2*4**(n - 1) # 우하단의 경우 우상단의 2배의 집을 지나쳐 옴
            #print(each_H)
            new_position = hilbert_position(n - 1, a - each_H) # n-1차 힐베르트 곡선에서 생각
            return [(new_position[0] + offset_H), (new_position[1] - offset_H)]  # 대각선 좌하단으로 이동해야 함
        elif a <= (4**n): # 좌하단
            tmp_x = 0 # 대칭이동 시키기 위한 변수
            tmp_y = 0
            offset_H = 2**(n - 1)
            each_H += 3*4**(n - 1)
            new_position = hilbert_position(n, a - each_H)
            tmp_x = (2**(n - 2) - 0.5) - new_position[0] # 대칭 이동하기 위한 계산
            tmp_y = -(2**(n - 2) - 0.5) - new_position[1]

            return [int(new_position[0] + 2*tmp_x), int(new_position[1] + 2*tmp_y - offset_H)] # 대칭 이동 시키고 offset 더해줌, float형이 되므로 int로 변환
        
def distant_H(pos1, pos2):
    ans = 0
    #print(pos1[0], pos1[1], pos2[0], pos2[1])
    ans = ((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)**(1/2)*10 # 한 칸단 10m
    ans = int(round(ans, 0))
    return ans 


# 입력부
num1 = int(input())
for p in range(num1):
    inp_num = input().split()
    n = int(inp_num[0])
    a = int(inp_num[1])
    b = int(inp_num[2])
    
    pos1 = hilbert_position(n, a)
    pos2 = hilbert_position(n, b)
    ans = distant_H(pos1, pos2)
    
    print(f'#{p+1} {ans}')

      
```

`각 테스트 케이스 마다 한 줄씩, 두 점 간의 거리를 미터 단위로 출력하라. 정수가 아닐 경우 가장 가까운 정수로 반올림해야 한다.` 라는 조건이 있으므로 `round`를 사용하도록 하자



### 고찰

1. 재귀를 평소 사용하지 않았던 터라 어떻게 구현할지를 생각하는지 조금 애먹었다.
2. 문제를 푸는 데 있어서 자신감이 붙은듯 하다.
3. 이번에 배운 html은 복습하긴 해야하는데, 조금 하기가 싫다.