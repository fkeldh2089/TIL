# SWEA_View

obj : 조망이 확보된 가구수를 구하시오

1. 여기서 조망이 확보되었다는 것은, 양옆으로 두 칸 같은 높이의 세대가 없다는 것을 의미한다. 
2. 이 때 최우측, 좌측 양단의 두 칸은 건물이 없다고 한다.
3. 입력은 건물의 높이가 연속적으로 주어진다.



### 1차

1. 양옆에 같은 층수가 없으면 된다, 해당 건물의 조망권이 확보된 가구수를 구하고 싶다면, 양옆의 높이를 두칸 뺀 후, 작은 수를 취하면 될 것이다. 이 때 작은 수가 음수라면 조망권이 확보된 가구는 없을 것이다.
2. 비교할 건물은 양단 2칸씩에는 존재하지 않는다

```python
def views(input_nums):
    view_sum = 0
    for i in range(2, len(input_nums)-2, 1):
        num1 = input_nums[i] - input_nums[i-1]
        num2 = input_nums[i] - input_nums[i+1]
        num3 = input_nums[i] - input_nums[i-2]
        num4 = input_nums[i] - input_nums[i+2]
        nums = [num1, num2, num3, num4]
        nums.sort()
        if nums[0] <= 0: # 가장 작은 수가 음수라면 조망권 없음
            view_B = 0
        else : # 모두 양수인 경우, 작은 수가 조망권을 갖고있는 수
            view_B = nums[0]

        view_sum +=view_B
    return view_sum
```

위와 같은 식으로 코드를 구현 할 것이다.

또 입력부의 경우

```python
n = int(input()) # 몇 번 반복할 것인지
for p in range(n):
    input_B = input().split() # 입력 받고
    input_nums = list(map(int, input_B)) # int의 리스트로 만들어서
    ans = views(input_nums) # 위의 함수에 입력
    print(f'#{p+1} ans') # 출력
```

이와 같이 만든다.



### 수정

입력부에서 몇 번 반복할 것인지 입력할 필요가 없다.

```python
for p in range(10):
    n = int(input()) # 몇 번 반복할 것인지
    input_B = input().split() # 입력 받고
    input_nums = list(map(int, input_B)) # int의 리스트로 만들어서
    ans = views(input_nums) # 위의 함수에 입력
    print(f'#{p+1} {ans}') # 출력
```

