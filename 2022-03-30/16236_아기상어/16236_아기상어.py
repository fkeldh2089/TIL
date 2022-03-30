# 16236 아기 상어
import sys
from pprint import pprint
sys.stdin = open('input_16236.txt')
from collections import deque

dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def BFS(r, c, field, shark):
    visited = [[0] * N for _ in range(N)]
    eat = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    stack = deque([[r, c]])
    tmp = 0
    while stack:
        r, c = stack.popleft()
        if tmp == visited[r][c]:
            break
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0 and (field[nr][nc] == shark or field[nr][nc] == 0):
                    visited[nr][nc] = visited[r][c] + 1
                    stack.append([nr, nc])
                elif visited[nr][nc] == 0 and field[nr][nc] < shark:  # 고기 발견 시
                    visited[nr][nc] = visited[r][c] + 1
                    tmp = visited[r][c] + 1
                    eat[nr][nc] = visited[r][c]

    for q1 in range(N):
        for q2 in range(N):
            if eat[q1][q2] != 0:
                return [q1, q2, eat[q1][q2]]
    return [0, 0, 0]  # 고기 발견 못하면, 0




N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
shark = 2
cnt = 0
feed = 0
fish = [0]*7
ans = [0, 0, 1]
hours = 0
for q1 in range(N):
    for q2 in range(N):
        if field[q1][q2] == 9:
            r, c = q1, q2
            field[q1][q2] = 0
        elif 0 < field[q1][q2] <= 6:
            fish[field[q1][q2]] += 1

while ans[2]:
    ans = BFS(r, c, field, shark)
    hours += ans[2]
    r, c = ans[0], ans[1]
    field[r][c] = 0
    feed += 1
    if feed == shark:
        shark += 1
        feed = 0
    # print(ans, shark)
    # pprint(field)
print(hours)