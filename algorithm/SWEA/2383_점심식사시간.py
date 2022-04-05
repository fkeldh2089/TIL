# 2383 점심 식사시간
import sys
sys.stdin = open('input_2383.txt')
from collections import deque


def sta_time(sta, poss):
    down_time = sta[2]  # 계단 내려가는 시간
    go_time = []  # 계단까지 시간
    for p in range(len(poss)):
        pos = poss[p]
        go_time.append(abs(pos[0]-sta[0]) + abs(pos[1]-sta[1]))  # 계단으로 가는 시간
    go_time.sort()
    go_time = deque(go_time)
    t = 0
    f = [0, 0, 0]
    qu = 0
    # print(sta, go_time)
    while go_time or f != [0, 0, 0] or qu:
        while go_time and go_time[0] == t:
            go_time.popleft()
            qu += 1
        # print(go_time)
        # print(t, f, qu)
        for q1 in range(3):
            if f[q1] > 0:
                f[q1] -= 1
        while qu > 0:
            for q1 in range(3):
                if f[q1] == 0:
                    f[q1] += down_time
                    qu -= 1
                    break
            else:
                break

        t += 1
    return t


TC = int(input())

for p in range(TC):
    N = int(input())  # 방 크기
    field = [list(map(int, input().split())) for _ in range(N)]
    peo = []
    sta = []
    mn = 5000
    cnt1 = 0  # 사람 수
    for q1 in range(N):
        for q2 in range(N):
            if field[q1][q2] == 1:  # 사람 위치 추가
                peo.append([q1, q2])
                cnt1 += 1
            elif field[q1][q2] != 0:  # 계단 [위치, 길이]
                sta.append([q1, q2, field[q1][q2]])

    for q in range(2 ** cnt1):  # 10101010
        sta0 = []
        sta1 = []  # 어디로 갈지 정해주는 리스트
        for q1 in range(cnt1):
            if 1 << q1 & q:
                sta0.append(peo[q1])
            else:
                sta1.append(peo[q1])
        # print(sta0, sta1)
        # sta1 = [[0, 3], [1, 2], [2, 1], [3, 4], [3, 3], [1, 4], [3, 2]]
        # sta0 = [[1, 3], [2, 4], [2, 2]]
        # sta0 = [peo[0], peo[1], peo[2]]
        # sta1 = [peo[3], peo[4], peo[5]]
        a = sta_time(sta[0], sta0)
        b = sta_time(sta[1], sta1)
        # print(a, b)
        if a <= b < mn:
            mn = b
        elif b <= a < mn:
            mn = a

    print(f'#{p+1} {mn}')
