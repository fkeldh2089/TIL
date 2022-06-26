# SWEA_Teleport

obj : 일방통행으로 연결되어 있는 텔레포트 장치를 통해 K 번 안에 갈 수 있는 별들의 갯수를 구하자

```python
"""
input
1 # 테스트 케이스를 몇번 반복할 것인지
5 2 # 총 5개의 행성에서 2번내로 갈 수 있는 별을 구하자
5 # 1번 별에서 5번 별로....
1
4
3
2

output
#1 38
```



### 알고리즘 구상

위의 테스트 케이스를 이용해 간단하게 생각해 보자

1. 먼저 [[1, 5], [2, 1]...]와 같이 [출발지, 도착지]로 이루어진 리스트를 갖는 리스트를 만들고
2. 반복문을 이용하여 
   - 1에서 시작하면, [1, 5, 2, 1...] 이런식으로 k+1개(이동 횟수) 꼬리를 무는 리스트를 만든다.
   - 1~N개를 반복한 후, 각 리스트를 set으로 변환하면, k번 이동시 도착 가능한 별의 갯수가 된다.



### 입력부 및 데이터 정리부

```python
n = int(input()) # 테스트 케이스 반복
for test_case in range(n):
    nums = input().split() # 별의 갯수와 이동 횟수 입력
    nums_list = list(map(int, nums))
    Stars = nums_list[0] # 별 갯수 Stars
    opper = nums_list[1] # 이동 횟수 opper
    tele_map = []
    for p in range(Stars):
        destination = int(input())
        tele_map.append([p+1, destination]) # [출발지, 도착지]리스트 생성        
```





### 계산부

```python
def calc_sum(nums, k):
    a = 1
    k_c = 0
    cnt = 0
    ansb = []
    sum1 = 0

    while cnt < len(nums):
        a = cnt + 1
        tmp = []
        k_c = 0
        tmp.append(a)
        r = 0
        while r < len(nums):
            if nums[r][0] == a:
                tmp.append(nums[r][1])
                a = nums[r][1]
                k_c += 1
                #print(f'#{cnt+1} {tmp}')
                r = 0
            else:
                r += 1
            if k_c == k:
                break
        b = len(set(tmp))
        
        cnt += 1
        ansb.append(b*cnt)
        #print(f'#{cnt} cococo {ansb}')
        
    for p in ansb:
        sum1 += p
    return sum1
                    
```

될듯 하다



### 제출용

```python
def calc_sum(nums, k):
    a = 1
    k_c = 0
    cnt = 0
    ansb = []
    sum1 = 0

    while cnt < len(nums):
        a = cnt + 1
        tmp = []
        k_c = 0
        tmp.append(a)
        r = 0
        while r < len(nums):
            if nums[r][0] == a:
                tmp.append(nums[r][1])
                a = nums[r][1]
                k_c += 1
                #print(f'#{cnt+1} {tmp}')
                r = 0
            else:
                r += 1
            if k_c == k:
                break
        b = len(set(tmp))
        
        cnt += 1
        ansb.append(b*cnt)
        #print(f'#{cnt} cococo {ansb}')
        
    for p in ansb:
        sum1 += p
    return sum1
                    

n = int(input()) # 테스트 케이스 반복
for test_case in range(n):
    nums = input().split() # 별의 갯수와 이동 횟수 입력
    nums_list = list(map(int, nums))
    Stars = nums_list[0] # 별 갯수 Stars
    opper = nums_list[1] # 이동 횟수 opper
    tele_map = []
    for p in range(Stars):
        destination = int(input())
        tele_map.append([p+1, destination]) # [출발지, 도착지]리스트 생성 
    print(f'#{test_case + 1} {calc_sum(tele_map, opper)}')
        

```

어느정도 동작은 하는듯 하지만, 동작시간이 너무 길다.