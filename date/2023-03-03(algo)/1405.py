#1405 미친 로봇
import sys
sys.stdin = open("input_1405.txt")


from collections import deque


inputs = list(map(int, input().split()))
N = inputs[0]
dir = inputs[1:]
ans = 0
field = [[0]*30 for _ in range(30)]

q = deque()
q.append([15, 15, 100**N, 0, 0])
field[15][15] = 1
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def DFS(r, c, per, cnt):
    global ans, N, dir
    if cnt == N:
        ans += per
        return 0
    for d in range(4):
        nr ,nc = r+dr[d], c+dc[d]
        if not(field[nr][nc]):
            field[nr][nc] = 1
            DFS(nr, nc, per/100*dir[d], cnt + 1)
            field[nr][nc] = 0
DFS(15,15,100**N,0)
# while q:
#     r, c, per, cnt, d = q[-1]
#     if d == 4:
#         q.pop()
#         field[r][c] = 0
#     else:
#         nr, nc = r+dr[d], c+dc[d]
#         nper = dir[d]
#         if field[nr][nc]:
#             q[-1][-1] += 1
#         else:
#             if cnt + 1 == N:
#                 ans += per/100*nper
#                 q[-1][-1] += 1
#             else:
#                 q[-1][-1] += 1
#                 field[nr][nc] = 1
#                 q.append([nr, nc, per/100*nper, cnt+1, 0])
print(ans/(100**N))

