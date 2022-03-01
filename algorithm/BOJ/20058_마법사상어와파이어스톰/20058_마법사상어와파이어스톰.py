# 20057 마법사 상어와 파이어스톰
import sys
from collections import deque
import pprint
sys.stdin = open('input_20058.txt')


def tornado(N, Q):  # field 에서 2^Q 의 격자크기로 회전
    global field
    op = N//Q
    for p1 in range(op):
        for p2 in range(op):
            tmp_mat = [field[p3][p2*Q:(p2+1)*Q] for p3 in range(p1*Q, (p1+1)*Q)]
            for r1 in range(Q):
                for r2 in range(Q):
                    field[r1+p1*Q][r2+p2*Q] = tmp_mat[-1-r2][r1]


def ice_break(N):  # 얼음 녹이기
    global field
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    ices = [[0]*N for _ in range(N)]  # 카운트 집어넣을 곳
    for p1 in range(N):
        for p2 in range(N):
            now_pos = [p1, p2]
            for p in range(4):
                new_pos = [dr[p] + now_pos[0], dc[p] + now_pos[1]]
                if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:
                    if field[new_pos[0]][new_pos[1]] > 0:  # 주위에 얼음이 있을 경우
                        ices[p1][p2] += 1
    for p1 in range(N):
        for p2 in range(N):
            if ices[p1][p2] < 3 and field[p1][p2] > 0:
                field[p1][p2] -= 1


def ice_mount(N):  # 얼음 덩어리
    global field
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    twice = [[0]*(N) for _ in range(N)]  # 중복 방지
    max_num = 0
    for p1 in range(N):  # 모든 좌표에 대하여
        for p2 in range(N):
            if twice[p1][p2] == 0 and field[p1][p2] == 1:
                mountain = deque()
                now_pos = [p1, p2]
                mountain.append(now_pos)
                twice[p1][p2] = 1
                idx1 = 0
                while 1:  # 길이 끊길 때 까지 반복
                    idx = idx1
                    idx1 = len(mountain)
                    for r in range(idx, len(mountain)):
                        for p in range(4):  # 4가지 방향에 대하여
                            new_pos = [dr[p] + mountain[r][0], dc[p] + mountain[r][1]]
                            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 필드 범위안에 들어가고
                                if field[new_pos[0]][new_pos[1]] >= 1 and twice[new_pos[0]][new_pos[1]] == 0:  # 얼음
                                    mountain.append(new_pos)  # 마운틴에 추가
                                    twice[new_pos[0]][new_pos[1]] = 1
                    if len(mountain) == idx1:  # 마운틴 수가 증가하지 않았다면, break
                        break
                if max_num < idx1:
                    max_num = idx1

    return max_num


# N은 필드의 크기 2^N, Qs는 격자의 크기, M은 횟수
N, M = list(map(int, input().split()))
N = 2**N
field = [list(map(int, input().split())) for _ in range(N)]
if M == 1:
    Q = int(input())
    Qs = [Q]
else:
    Qs = list(map(int, input().split()))
for p in range(M):
    Q = 2**Qs[p]
    tornado(N, Q)
    # pprint.pprint(field)
    ice_break(N)
    # pprint.pprint(field)
ans = 0
for p1 in range(N):
    for p2 in range(N):
        ans += field[p1][p2]

max_num = ice_mount(N)
print(ans)
print(max_num)

