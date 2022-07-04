# 3109 빵집
import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input_3109.txt')


def DFS(r, c):
    for d in range(3):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] and field[nr][nc] == '.':
            visited[nr][nc] = 0
            if nc == C-1 or DFS(nr, nc):
                return 1
    return 0


R, C = map(int, input().split())
field = [input() for _ in range(R)]
visited = [[1] * C for _ in range(R)]
dr = [-1, 0, 1]
dc = [1, 1, 1]

cnt = 0
for p in range(R):
    visited[p][0] = 0
    if DFS(p, 0):
        cnt += 1
print(cnt)