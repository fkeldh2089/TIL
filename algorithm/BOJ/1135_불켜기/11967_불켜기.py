# 11967 불켜기
import sys
from collections import defaultdict, deque
sys.stdin = open('input_11967.txt')


def canmove(r, c):
    stack2 = deque()
    stack2.append([r, c])
    visited2 = [[1]*(N+1) for _ in range(N+1)]
    visited2[1][1] = 0
    while stack2:
        r, c = stack2.popleft()
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 1<= nr < N+1 and 1<= nc < N+1 and visited2[nr][nc] and lighten[1000 * nr + nc]:
                if field[1000 * nr + nc] == 0:
                    stack.append(1000 * nr + nc)
                    field[1000 * nr + nc] = 1
                visited2[nr][nc] = 0
                stack2.append([nr, nc])
        # print(f'stack2: {stack2}')


N, M = map(int, input().split())
switches = defaultdict(list)
lighten = defaultdict(int)
field = defaultdict(int)
visited = [[1]*(N+1) for _ in range(N+1)]
lighten[1001] = 1
field[1001] = 1
visited[1][1] = 0
stack = deque()
stack.append(1001)

for p in range(M):
    x, y, a, b = map(int, input().split())
    switches[1000*x+y].append(1000*a+b)

cnt = 1
while stack:
    tmp = stack.popleft()
    if switches[tmp]:
        for p in switches[tmp]:
            if not lighten[p]:
                lighten[p] = 1
                cnt += 1
    canmove(1, 1)  # 이동가능한 곳 확장
print(cnt)