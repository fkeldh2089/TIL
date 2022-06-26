# 5105 미로의 거리
import sys
from pprint import pprint
sys.stdin = open('input_5105.txt')


def BFS():
    global ans
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    while stack:
        r, c = stack.pop(0)
        for p in range(4):
            nr, nc = r + dr[p], c + dc[p]
            if 0 <= nr < N and 0 <= nc < N:
                if field[nr][nc] == 0:
                    stack.append([nr, nc])
                    field[nr][nc] = field[r][c] - 1
                if field[nr][nc] == 3:
                    ans = field[r][c]
                    return
        # pprint(field)


TC = int(input())
for p in range(TC):
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(N)]
    ans = 0

    for q1 in range(N):
        for q2 in range(N):
            if field[q1][q2] == 2:
                pos = [q1, q2]
                field[q1][q2] = 0

    stack = [pos]
    BFS()
    print(f'#{p+1} {-ans}')