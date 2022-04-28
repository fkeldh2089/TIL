import sys
from pprint import pprint
sys.stdin = open('input.txt')
from collections import deque


def BFS(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    stack.append([r,c])
    while stack:
        r, c = stack.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] > visited[r][c] + field[nr][nc]:
                    visited[nr][nc] = visited[r][c] + field[nr][nc]
                    stack.append([nr, nc])


TC = int(input())
for p in range(TC):
    N = int(input())
    field = [list(map(int, list(input())))for _ in range(N)]
    visited = [[1000000]*N for _ in range(N)]
    visited[0][0] = 0
    stack = deque()
    BFS(0, 0)
    print(f'#{p+1} {visited[N - 1][N - 1]}')
