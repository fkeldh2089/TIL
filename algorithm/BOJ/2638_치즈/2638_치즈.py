# 2638_치즈
import sys
from pprint import pprint
from collections import deque
sys.stdin = open('input_2638.txt')


def BFS(r, c):
    # print(f'BFS: {r, c}')
    global cheesed
    stack = deque()
    stack.append([r, c])
    visited = [[0] * M for _ in range(N)]
    visited[r][c] = 1
    cheesed = [[0] * M for _ in range(N)]
    while stack:
        r, c = stack.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                if cheese[nr][nc] == 0 and visited[nr][nc] == 0:
                    stack.append([nr, nc])
                    visited[nr][nc] = 1
                elif cheese[nr][nc]:
                    cheesed[nr][nc] += 1
    return True


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
cheesed = [[0] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
block = []
for p1 in range(N):
    for p2 in range(M):
        if cheese[p1][p2]:
            block.append([p1, p2])

i = 0
f = 1
idx = []
while(f):
    f= 0
    BFS(0, 0)
    for p1 in range(N):
        for p2 in range(M):
            if cheesed[p1][p2]>=2:
                cheese[p1][p2] = 0
                f = 1
    # pprint(cheese)
    i += 1

print(i-1)
