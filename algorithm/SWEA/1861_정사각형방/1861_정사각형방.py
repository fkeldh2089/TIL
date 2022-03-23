# 1861 정사각형 방
import sys
sys.stdin = open('input_1861.txt')
from collections import deque


def BFS(si, sj):
    q = []
    s = []

    q.append([si, sj])
    v[si][sj] = 1
    s.append(field[si][sj])
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and abs(field[ci][cj] - field[ni][nj]) == 1:
                q.append((ni, nj))
                v[ni][nj]=1
                s.append(field[ni][nj])
    return min(s), len(s)


TC = int(input())

for p in range(TC):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    num = N*N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                tn, tc = BFS(i, j)
                if cnt < tc or cnt == tc and num > tn:
                    cnt = tc
                    num = tn

    print(f'#{p+1} {num} {cnt}')