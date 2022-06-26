# [S/W 문제해결 응용] 2일차 - 최대 상금

obj : 숫자를 입력 받고, 주어진 횟수만큼 자릿수끼리 교환하여 최대의 숫자를 만들어내자!

#### 처음 생각한 것은 간단하게 

```python
# 1-1. 입력부
number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
number_list = list(number[0]) # 교환할 숫자
opper = number[1] # 교환 가능 횟수
number1 = number_list[::]
number_list.sort(reverse = True)
goal = number[::] # 목표로할 숫자
```

- 입력받은 숫자를 리스트로 변환시킨다
- 목표로할 최대 숫자를 지정한다.

```python
# 2-1. 교환부
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        tmp = number1[p]
        number1[p] = goal[p]
        for q in range(len(number1)):
            if tmp = number1[-1-q]:
                number1[-1-q] = tmp
```

- 제일 위의 자릿수에서 부터 목표로 한 숫자와 맞춰주도록 한다.
- 주어진 횟수만큼 반복한다.

```python
# 3-1. 나머지
if number1 == goal: # 목표와 같은 숫자가 된다면,
    for p in range(len(opper - {'이미 한 횟수'})):
        number1[-1], number1[-2] = number1[-2], number1[-1] # 가장 작은 두 수를 계속 교환한다.
```

=> 결과적으로 가장 강력하고 간단한 코드인데, 몇 개의 예외처리에 있어 약점을 보인다. 예를들어

`32888 2`를 입력받을 경우, 위의 코드에 의하면 `88823`이 출력된다. 하지만 이 경우 `88832`가 출력되어야 한다. 

또 `77776 1`의 경우, `77767`로 잘못된 값을 계산한다. 이와 같은 오류의 원인으로는

- 중복된 숫자가 있고, 교환 기회가 여러 충분할 경우, 따로따로 교환하는 것이 아닌 한번에 가장 큰 숫자로 바뀔 수 있어야 한다.
- 중복된 숫자가 있을 경우, 교환 기회가 많이 남을 경우, 같은 숫자끼리 교환하면 값의 변동이 없을 수 있다.



#### 두번째로 생각한 것

obj : 위의 토대를 들고 가되 중복되는 숫자에 대한 예외처리를 구현하자

1. 먼저 입력부는 내버려 두고, 교환부 먼저 바꿔보도록 합시다.

```python
# 2-2. 교환부
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        if number1.count(number[p]) == 1: # 가장 큰 숫자중 중복된 숫자가 없을 경우
            tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
            number1[p] = goal[p]
            
            for q in range(len(number1)):
                if tmp = number1[-1-q]:
                    number1[-1-q] = tmp
```

- 바꿀 숫자중에 중복이 없으면 다음과 같이 진행하도록 한다. 하지만 이 방법에도 문제가 있는데,,,
  - number1전체에서 중복을 찾게되면, 이미 교환할 필요가 없는 숫자도 포함해 버린다.
    - 교환해야할 숫자들을 먼저 리스트화 시켜놓도록 해야겠다
  - 교환 횟수가 1일 경우 중복을 신경 쓸 필요가 없고, 교환횟수에 따라 중복된 숫자의 포함 여부를 확인
    - 잔여 교환 횟수와, 중복된 숫자의 개수를 비교 확인 할 필요가 있다.



2. 입력부에서 위 사항을 해결하기 위한 조치를 합시다.

```python
# 1-2. 입력부
number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
number_list = list(number[0]) # 교환할 숫자
opper = number[1] # 교환 가능 횟수
number1 = number_list[::]
number_list.sort(reverse = True)
goal = number[::] # 목표로할 숫자

to_c = [] # 교환이 필요한 숫자들의 리스트
try_c = 0 # 사용한 교환 횟수

for p in range(len(number1)): # 교환이 필요한 경우 to_c에 추가
    if number1[p] != goal[p]:
        to_c.append(number[p])
```

3. 교환부에서 해결을 위한 조치를 합시다.

```python
# 2-2. 교환부 (교환 숫자가 중복이 없을 경우)
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        if to_c.count(goal[p]) == 1: # 교환할 큰 숫자가 중복된 숫자가 없을 경우
            tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
            number1[p] = goal[p]
            try_c += 1 # 교환 시도 횟수 증가
            
            for q in range(len(number1)):
                if tmp = number1[-1-q]:
                    number1[-1-q] = tmp
```

- 중복이 없을 경우는 동작할 것이다.

4. 교환할 숫자가 중복이 될 경우,

```python
# 2-2. 교환부 (교환 숫자가 중복이 있을 경우)
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        elif to_c.count(goal[p]) > 1: # 교환할 큰 숫자가 중복된 숫자가 있을 경우
            if (opp-try_c) >= to_c.count(goal[p]): # 잔여 교환 횟수가 더 클 경우
                tmp = to_c[-1:-1 - to_c.count(goal[p]): -1 ] # 교환해야 할 수 저장
                tmp.sort() # 교환해야할 숫자 오름차순으로 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) #교환 시도 횟수 증가
            
            elif (opp-try_c) < to_c.count(goal[p]): # 잔여 횟수가 적을 경우
                tmp = to_c[-1:-1 - (opp-try_c):-1] # 교환 해야할 수 저장
                tmp.sort() # 교환해야할 수 오름차순 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) # 교환 시도 횟수 증가
```

- 돌려 보기 전에도 한가지 오류가 떠오른다.
  - to_c를 갱신해 주지 않는 다면 오류가 발생할 확률이 높다
    - to_c를 만드는 함수를 만들어, 지속적으로 갱신해주자

```python
# 1-2. 입력부
number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
number_list = list(number[0]) # 교환할 숫자
opper = number[1] # 교환 가능 횟수
number1 = number_list[::]
number_list.sort(reverse = True)
goal = number[::] # 목표로할 숫자

to_c = [] # 교환이 필요한 숫자들의 리스트
try_c = 0 # 사용한 교환 횟수

def make_to_c(number1, goal): # to_c를 반환하는 함수
    to_c = []
    for p in range(len(number1)): # 교환이 필요한 경우 to_c에 추가
        if number1[p] != goal[p]:
            to_c.append(number[p])
    return to_c
```

```python
# 2-2. 교환부 (교환 숫자가 중복이 없을 경우)
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        if to_c.count(goal[p]) == 1: # 교환할 큰 숫자가 중복된 숫자가 없을 경우
            tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
            number1[p] = goal[p]            
            for q in range(len(number1)):
                if tmp = number1[-1-q]:
                    number1[-1-q] = tmp
            
            try_c += 1 # 교환 시도 횟수 증가
            to_c = make_to_c(number1, goal) # to_c 갱신
```

```python
# 2-2. 교환부 (교환 숫자가 중복이 있을 경우)
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        elif to_c.count(goal[p]) > 1: # 교환할 큰 숫자가 중복된 숫자가 있을 경우
            if (opp-try_c) >= to_c.count(goal[p]): # 잔여 교환 횟수가 더 클 경우
                tmp = to_c[-1:-1 - to_c.count(goal[p]): -1 ] # 교환해야 할 수 저장
                tmp.sort() # 교환해야할 숫자 오름차순으로 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) #교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
            
            elif (opp-try_c) < to_c.count(goal[p]): # 잔여 횟수가 적을 경우
                tmp = to_c[-1:-1 - (opp-try_c):-1] # 교환 해야할 수 저장
                tmp.sort() # 교환해야할 수 오름차순 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) # 교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
```

교환부를 합치면,

```python
# 2-2. 교환부 (교환 숫자가 중복이 없을 경우)
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        if to_c.count(goal[p]) == 1: # 교환할 큰 숫자가 중복된 숫자가 없을 경우
            tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
            number1[p] = goal[p]            
            for q in range(len(number1)):
                if tmp = number1[-1-q]:
                    number1[-1-q] = tmp
            
            try_c += 1 # 교환 시도 횟수 증가
            to_c = make_to_c(number1, goal) # to_c 갱신
            
        elif to_c.count(goal[p]) > 1: # 교환할 큰 숫자가 중복된 숫자가 있을 경우
            if (opp-try_c) >= to_c.count(goal[p]): # 잔여 교환 횟수가 더 클 경우
                tmp = to_c[-1:-1 - to_c.count(goal[p]): -1 ] # 교환해야 할 수 저장
                tmp.sort() # 교환해야할 숫자 오름차순으로 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) #교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
            
            elif (opp-try_c) < to_c.count(goal[p]): # 잔여 횟수가 적을 경우
                tmp = to_c[-1:-1 - (opp-try_c):-1] # 교환 해야할 수 저장
                tmp.sort() # 교환해야할 수 오름차순 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) # 교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
```

5. 이 교환 횟수, 혹은 목표를 달성했을 경우의 처리를 구현하자

```python
if try_c == opp:
    return number1 # 횟수가 없으므로 그대로 출력
if goal == number1:
    break
```

6. 나머지 횟수를 처리해야 할 경우

```python
# 3-2. 나머지
if number1 == goal: # 목표와 같은 숫자가 된다면,
    if len(set(number1)) != len(number1): # 중복되는 숫자가 있다면
        return number1 # 값이 더 이상 바뀌지 않을 것이다
    else :
        if (opp-try_c)%2: # 남은 횟수가 홀수면,
            number1[-1], number1[-2] = number1[-2], number1[-1] 
            return number1 # 한 번 바꾸고 출력
        else:
            return number1 # 짝수면 그대로 출력
```

7. 모든 코드를 합쳐 보면

```python
# 1-2. 입력부
number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
number_list = list(number[0]) # 교환할 숫자
opper = number[1] # 교환 가능 횟수
number1 = number_list[::]
number_list.sort(reverse = True)
goal = number[::] # 목표로할 숫자

to_c = [] # 교환이 필요한 숫자들의 리스트
try_c = 0 # 사용한 교환 횟수

def make_to_c(number1, goal): # to_c를 반환하는 함수
    to_c = []
    for p in range(len(number1)): # 교환이 필요한 경우 to_c에 추가
        if number1[p] != goal[p]:
            to_c.append(number[p])
    return to_c


# 2-2. 교환부 (교환 숫자가 중복이 없을 경우)
for p in range(len(number1)): # 
    if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
        if to_c.count(goal[p]) == 1: # 교환할 큰 숫자가 중복된 숫자가 없을 경우
            tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
            number1[p] = goal[p]            
            for q in range(len(number1)):
                if tmp = number1[-1-q]:
                    number1[-1-q] = tmp
            
            try_c += 1 # 교환 시도 횟수 증가
            to_c = make_to_c(number1, goal) # to_c 갱신
            
        elif to_c.count(goal[p]) > 1: # 교환할 큰 숫자가 중복된 숫자가 있을 경우
            if (opp-try_c) >= to_c.count(goal[p]): # 잔여 교환 횟수가 더 클 경우
                tmp = to_c[-1:-1 - to_c.count(goal[p]): -1 ] # 교환해야 할 수 저장
                tmp.sort() # 교환해야할 숫자 오름차순으로 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) #교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
            
            elif (opp-try_c) < to_c.count(goal[p]): # 잔여 횟수가 적을 경우
                tmp = to_c[-1:-1 - (opp-try_c):-1] # 교환 해야할 수 저장
                tmp.sort() # 교환해야할 수 오름차순 정렬
                for q in range(len(tmp)):
                    for r in range(len(number1)):
                        if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                            number[-r] = tmp[r] # 교환
                            break # 한번 바꾸면 탈출
                for q in range(len(tmp)):
                    for r in range(number1):
                        if number[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                        	number[r] = goal[p] # 교환
                            break # 한번 바꾸면 탈출
                try_c += len(tmp) # 교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
                
# 3-2. 나머지               
	if try_c == opp:
    	return number1 # 횟수가 없으므로 그대로 출력
	if number1 == goal: # 목표와 같은 숫자가 된다면,
    	if len(set(number1)) != len(number1): # 중복되는 숫자가 있다면
        	return number1 # 값이 더 이상 바뀌지 않을 것이다
    	else :
        	if (opp-try_c)%2: # 남은 횟수가 홀수면,
            	number1[-1], number1[-2] = number1[-2], number1[-1] 
            	return number1 # 한 번 바꾸고 출력
        	else:
            	return number1 # 짝수면 그대로 출력
```



#### 실행 및 디버그

obj  : 코드를 돌려보면서 자료의 타입이나, 자잘한 오타를 고친다.

```python
# 함수 설정

def make_to_c(number1, goal): # to_c를 반환하는 함수
    to_c = []
    for p in range(len(number1)): # 교환이 필요한 경우 to_c에 추가
        if number1[p] != goal[p]:
            to_c.append(number1[p])
    return to_c


# 교환부 (교환 숫자가 중복이 없을 경우)
def change_num(number1, goal, opper):
    try_c = 0 # 사용한 교환 횟수
    to_c = make_to_c(number1, goal)
    print(f'#{try_c} : {to_c}')
    print(f'#{try_c} : opper = {opper}, try_c = {try_c}')
    for p in range(len(number1)): # 
        if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
            if to_c.count(goal[p]) == 1: # 교환할 큰 숫자가 중복된 숫자가 없을 경우
                tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
                number1[p] = goal[p]            
                for q in range(len(number1)):
                    if number1[-1-q] == goal[p]:
                        number1[-1-q] = tmp
                        break

                try_c += 1 # 교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신
                #print(f'#{try_c} : {to_c}')
                #print(f'#{try_c} : {number1}')

            elif to_c.count(goal[p]) > 1: # 교환할 큰 숫자가 중복된 숫자가 있을 경우
                if (opper-try_c) >= to_c.count(goal[p]): # 잔여 교환 횟수가 더 클 경우
                    tmp = to_c[0:to_c.count(goal[p]):1] # 교환해야 할 수 저장
                    tmp.sort() # 교환해야할 숫자 오름차순으로 정렬
                    
                    print(f'#{try_c} tmp: {tmp}')
                    
                    for q in range(len(tmp)):                        
                        for r in range(len(number1)):
                            if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                                number1[-r] = tmp[q] # 교환
                                break # 한번 바꾸면 탈출
                    for q in range(len(tmp)):
                        for r in range(len(number1)):
                            if number1[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                                number1[r] = goal[p] # 교환
                                break # 한번 바꾸면 탈출
                    try_c += len(tmp) #교환 시도 횟수 증가
                    to_c = make_to_c(number1, goal) # to_c 갱신

                elif (opper-try_c) < to_c.count(goal[p]): # 잔여 횟수가 적을 경우
                    tmp = to_c[0:(opper-try_c):1] # 교환 해야할 수 저장
                    tmp.sort() # 교환해야할 수 오름차순 정렬
                    
                    print(f'#{try_c} tmp: {tmp}')
                    
                    for q in range(len(tmp)):
                        for r in range(len(number1)):
                            if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                                number1[-r] = tmp[q] # 교환
                                break # 한번 바꾸면 탈출
                    for q in range(len(tmp)):
                        for r in range(len(number1)):
                            if number1[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                                number1[r] = goal[p] # 교환
                                break # 한번 바꾸면 탈출
                    try_c += len(tmp) # 교환 시도 횟수 증가
                    to_c = make_to_c(number1, goal) # to_c 갱신

                    
        print(type(opper), type(try_c))            
    # 나머지               
        if try_c == opper:
            return number1 # 횟수가 없으므로 그대로 출력
        if number1 == goal: # 목표와 같은 숫자가 된다면,
            if len(set(number1)) != len(number1): # 중복되는 숫자가 있다면
                return number1 # 값이 더 이상 바뀌지 않을 것이다
            else :
                if (opper - try_c)%2: # 남은 횟수가 홀수면,
                    number1[-1], number1[-2] = number1[-2], number1[-1] 
                    return number1 # 한 번 바꾸고 출력
                else:
                    return number1 # 짝수면 그대로 출력
```

```python
# 입력부
number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
number_list = list(map(int, list(number[0]))) # 교환할 숫자
opper = int(number[1]) # 교환 가능 횟수
number1 = number_list[::]
number_list.sort(reverse = True)
goal = number_list[::] # 목표로할 숫자
print(number1,opper,goal)
#to_c = [] # 교환이 필요한 숫자들의 리스트
#try_c = 0 # 사용한 교환 횟수

print(change_num(number1, goal, opper))
```

- 실행에 문제 없고, 각종 예외를 집어넣어도 잘 동작함, 문제의 input에 맞게 설정하도록 변경하자



#### 제출용 입력부 변환

obj : 입력과 출력을 문제에 맞게 맞춰주도록 한다.

```python
# 입력부
r_number = int(input())
for p in range(r_number):    
    number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
    number_list = list(map(int, list(number[0]))) # 교환할 숫자
    opper = int(number[1]) # 교환 가능 횟수
    number1 = number_list[::]
    number_list.sort(reverse = True)
    goal = number_list[::] # 목표로할 숫자

    result = change_num(number1, goal, opper)
    ans = ''.join(list(map(str, result)))
    print(f'#{p+1} {ans}')
```



#### 제출 코드

```python
def make_to_c(number1, goal): # to_c를 반환하는 함수
    to_c = []
    for p in range(len(number1)): # 교환이 필요한 경우 to_c에 추가
        if number1[p] != goal[p]:
            to_c.append(number1[p])
    return to_c


# 2-2. 교환부 (교환 숫자가 중복이 없을 경우)
def change_num(number1, goal, opper):
    try_c = 0 # 사용한 교환 횟수
    to_c = make_to_c(number1, goal)

    for p in range(len(number1)): # 
        if number1[p] != goal[p]: # 제일 큰 자릿 수부터 목표로한 금액과 차이가 잇으면 바꿔버린다.
            if to_c.count(goal[p]) == 1: # 교환할 큰 숫자가 중복된 숫자가 없을 경우
                tmp = number1[p] # 위의 처음 생각한 교환부의 기능을 그대로 가져간다.
                number1[p] = goal[p]            
                for q in range(len(number1)):
                    if number1[-1-q] == goal[p]:
                        number1[-1-q] = tmp
                        break

                try_c += 1 # 교환 시도 횟수 증가
                to_c = make_to_c(number1, goal) # to_c 갱신


            elif to_c.count(goal[p]) > 1: # 교환할 큰 숫자가 중복된 숫자가 있을 경우
                if (opper-try_c) >= to_c.count(goal[p]): # 잔여 교환 횟수가 더 클 경우
                    tmp = to_c[0:to_c.count(goal[p]):1] # 교환해야 할 수 저장
                    tmp.sort() # 교환해야할 숫자 오름차순으로 정렬
                    for q in range(len(tmp)):                        
                        for r in range(len(number1)):
                            if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                                number1[-r] = tmp[q] # 교환
                                break # 한번 바꾸면 탈출
                    for q in range(len(tmp)):
                        for r in range(len(number1)):
                            if number1[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                                number1[r] = goal[p] # 교환
                                break # 한번 바꾸면 탈출
                    try_c += len(tmp) #교환 시도 횟수 증가
                    to_c = make_to_c(number1, goal) # to_c 갱신

                elif (opper-try_c) < to_c.count(goal[p]): # 잔여 횟수가 적을 경우
                    tmp = to_c[0:(opper-try_c):1] # 교환 해야할 수 저장
                    tmp.sort() # 교환해야할 수 오름차순 정렬
                    for q in range(len(tmp)):
                        for r in range(len(number1)):
                            if number1[-r] == goal[p]: # number1 뒤에서부터 큰수를 가장 작은 수
                                number1[-r] = tmp[q] # 교환
                                break # 한번 바꾸면 탈출
                    for q in range(len(tmp)):
                        for r in range(len(number1)):
                            if number1[r] == tmp[q]: # 앞자리서 부터 바꿔줄 숫자 찾자
                                number1[r] = goal[p] # 교환
                                break # 한번 바꾸면 탈출
                    try_c += len(tmp) # 교환 시도 횟수 증가
                    to_c = make_to_c(number1, goal) # to_c 갱신

                            
    # 3-2. 나머지               
        if try_c == opper:
            return number1 # 횟수가 없으므로 그대로 출력
        if number1 == goal: # 목표와 같은 숫자가 된다면,
            if len(set(number1)) != len(number1): # 중복되는 숫자가 있다면
                return number1 # 값이 더 이상 바뀌지 않을 것이다
            else :
                if (opper - try_c)%2: # 남은 횟수가 홀수면,
                    number1[-1], number1[-2] = number1[-2], number1[-1] 
                    return number1 # 한 번 바꾸고 출력
                else:
                    return number1 # 짝수면 그대로 출력
                  
                  
                  
# 입력부
r_number = int(input())
for p in range(r_number):    
    number = input().split() # 1234 1 => 1234의 숫자를 입력, 1번 교환하여 가장 큰 숫자를 만들자
    number_list = list(map(int, list(number[0]))) # 교환할 숫자
    opper = int(number[1]) # 교환 가능 횟수
    number1 = number_list[::]
    number_list.sort(reverse = True)
    goal = number_list[::] # 목표로할 숫자

    result = change_num(number1, goal, opper)
    ans = ''.join(list(map(str, result)))
    print(f'#{p+1} {ans}')
```

