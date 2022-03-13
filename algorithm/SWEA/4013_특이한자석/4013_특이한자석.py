# 4013 특이한 자석
import sys
from pprint import pprint
sys.stdin = open('input_4013.txt')
from collections import deque

TC = int(input())

for p in range(TC):
    K = int(input())
    Gear = [deque(map(int, input().split())) for _ in range(4)]
    A = deque(Gear[0])
    B = deque(Gear[1])
    C = deque(Gear[2])
    D = deque(Gear[3])
    # [2]가 오른쪽, [6]이 왼쪽
    Move = [list(map(int, input().split())) for _ in range(K)]

    for q in range(K):  # 이동 횟수 만큼
        status = [0] * 4  # 톱니바퀴의 운동 상태
        status[Move[q][0]-1] = Move[q][1]

        nq = Move[q][0]-1
        while nq < 3 and status[nq] != 0:
            if Gear[nq][2] == Gear[nq+1][6]:  # 극성이 같다면,
                status[nq+1] = 0
            else:  # 극성이 다르다면,
                if status[nq] == 1:
                    status[nq + 1] = -1
                else:
                    status[nq + 1] = 1
            nq += 1

        nq = Move[q][0]-1
        while nq > 0 and status[nq] != 0:
            if Gear[nq][6] == Gear[nq - 1][2]:  # 극성이 같다면,
                status[nq - 1] = 0
            else:  # 극성이 다르다면,
                if status[nq] == 1:
                    status[nq - 1] = -1
                else:
                    status[nq - 1] = 1
            nq -= 1
        # pprint(Gear)
        # print(status)
        for q1 in range(4):
            Gear[q1].rotate(status[q1])
        # pprint(Gear)

    ans = 0
    for q in range(4):
        if Gear[q][0] == 1:
            ans += 2**q

    print(f'#{p+1} {ans}')



