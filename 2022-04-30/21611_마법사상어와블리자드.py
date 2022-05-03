import sys
from pprint import pprint
sys.stdin = open('input_21611.txt')

N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
pprint(field)
command = [list(map(int, input().split())) for _ in range(M)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c = 0, 0
d = 0
stack = [field[0][0]]
field[r][c] = -1
while 1:
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < N and 0 <= nc < N and field[nr][nc] != -1:
        stack.append(field[nr][nc])
        field[nr][nc] = -1
        r, c = nr, nc
        if r == N//2 and c == N//2:
            break
    else:
        d += 1
        d %= 4
stack.reverse()

print(stack)