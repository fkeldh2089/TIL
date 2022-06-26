#### 낚시터

```python
import sys
from pprint import pprint
sys.stdin = open('fishing.txt')
from copy import deepcopy


def move_to(fish_place, doors3, cnt):
    global N, mn
    # print(f'# {fish_place, doors3, cnt}')
    l = len(doors3)
    # print(f'l : {l}')
    if l == 0:
        # print(f'**{cnt}')
        if cnt < mn:
            mn = cnt
        return
    de_doors3 = deepcopy(doors3)  # 복사(백업)해 둡시다.
    # 각 문에 대하여, 순열을 만드는 느낌으로 반복문 설정, (0, 1, 2), (0, 2, 1), (1, 0, 2)....
    for p in range(l):  
        doors3 = deepcopy(de_doors3)  # 불러오고,
        doors = doors3.pop(p)  # 이번에 쓸 문 정보 불러오고,
        pos = doors[0]-1  # 문의 위치
        nums = doors[1]  # 사람 수
        tmp = []
        for q in range(N):
            if fish_place[q] == 0:  # [거리, 위치]
                tmp.append([abs(pos-q), q])
        tmp.sort()
        if len(tmp) > nums and tmp[nums-1][0] == tmp[nums][0]:  # 마지막에 거리가 같은 위치가 있다면,
            for q1 in range(2):
                if q1 == 0:
                    for q in range(nums):
                        fish_place[tmp[q][1]] = 1  # 거리가 작은 순서대로 자리를 채워간다.
                        cnt += tmp[q][0] + 1  # 거리 카운트
                    # print(q1, cnt, fish_place)
                    move_to(fish_place, doors3, cnt)
                    for q in range(nums):
                        fish_place[tmp[q][1]] = 0  # 거리가 작은 순서대로 자리를 채워간다.
                        cnt -= tmp[q][0] + 1  # 거리 카운트
                elif q1 == 1:
                    for q in range(nums-1):
                        fish_place[tmp[q][1]] = 1  # 거리가 작은 순서대로 자리를 채워간다.
                        cnt += tmp[q][0]+1  # 거리 카운트
                    fish_place[tmp[nums][1]] = 1
                    cnt += tmp[nums][0]+1
                    # print(cnt, fish_place)
                    move_to(fish_place, doors3, cnt)
                    for q in range(nums-1):
                        fish_place[tmp[q][1]] = 0  # 거리가 작은 순서대로 자리를 채워간다.
                        cnt -= tmp[q][0]+1  # 거리 카운트
                    fish_place[tmp[nums][1]] = 0
                    cnt -= tmp[nums][0]+1

        else:  # 아니라면
            if tmp:
                for q in range(nums):
                    fish_place[tmp[q][1]] = 1  # 거리가 작은 순서대로 자리를 채워간다.
                    cnt += tmp[q][0]+1  # 거리 카운트
                # print(cnt, fish_place)
                move_to(fish_place, doors3, cnt)
                for q in range(nums):
                    fish_place[tmp[q][1]] = 0  # 거리가 작은 순서대로 자리를 채워간다.
                    cnt -= tmp[q][0]+1  # 거리 카운트



TC = int(input())

for p in range(TC):
    N = int(input())
    doors = [list(map(int, input().split())) for _ in range(3)]  # [위치, 숫자]
    mn = 500000
    fish_place = [0] * N

    move_to(fish_place, doors, 0)

    print(f'#{p+1} {mn}')
```



#### 사냥

```python
import sys
from pprint import pprint
sys.stdin = open('hunt.txt')
from copy import deepcopy


def odn(mons, nums):
    global mn
    # if len(nums) == cnt1 * 2:
    #     print(f'**최종** : {nums}')
    de_mons = deepcopy(mons)
    de_nums = deepcopy(nums)
    l = len(mons)

    # 몬스터 좌표를 경로 후보에 포함, 이후 경로 확정 시, 몬스터일 경우 경로 후보에 고객을 포함,
    for q in range(l):
        mons = deepcopy(de_mons)
        nums = deepcopy(de_nums)
        tmp_mons = mons.pop(q)
        nums.append(tmp_mons)
        if field[tmp_mons[1]][tmp_mons[2]] > 0:  # 몬스터이면,,
            tmp = field[tmp_mons[1]][tmp_mons[2]]  # 몬스터 숫자
            for q1 in range(cnt1):
                if guest[q1][0] == tmp:  # 고객을 찾아서
                    mons.append(guest[q1])  # 경로 후보에 추가
                    break
        # print(f'경로 설정 : {q}{nums}')
        # print(f'경로 후보 : {mons}')
        if len(nums) == cnt1 * 2 or mons == []:
            # print(f'**최종** : {nums}')
            ans = 0
            r, c = 0, 0
            for q2 in range(cnt1 * 2):
                ans += abs(r-nums[q2][1]) + abs(c-nums[q2][2])
                r, c = nums[q2][1], nums[q2][2]
            if ans < mn:
                mn = ans
                # print(f'경로 설정 : {q}{nums}')
                # print(f'경로 후보 : {mons}, {ans}')
            return
        odn(mons, nums)







TC = int(input())
for p in range(TC):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    # pprint(field)

    monster = []
    guest = []
    cnt1 = 0
    for q1 in range(N):  # 필드 위의 몬스터와 손님 정렬
        for q2 in range(N):
            if field[q1][q2] > 0:
                monster.append([field[q1][q2], q1, q2])
                cnt1 += 1
            elif field[q1][q2] < 0:
                guest.append([-field[q1][q2], q1, q2])

    monster.sort()  # 정렬
    guest.sort()
    # print(f'monster : {monster}')
    # print(f'guest : {guest}')
    mons = deepcopy(monster)
    nums = []
    mn = 400
    odn(mons, nums)
    print(f'#{p+1} {mn}')

```

