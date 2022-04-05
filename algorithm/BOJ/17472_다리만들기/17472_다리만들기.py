# 17472 다리만들기
import sys
from pprint import pprint
sys.stdin = open('input_17472.txt')


def BFS():
    stack = []
    cnt = 0
    for q1 in range(N):
        for q2 in range(M):
            if field[q1][q2] and visited[q1][q2] == 0:
                stack.append([q1, q2])
                cnt += 1
                field[q1][q2] = cnt
            while stack:
                r, c = stack.pop()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and field[nr][nc] == 1 and visited[nr][nc]==0:
                        field[nr][nc] = cnt
                        visited[nr][nc] = 1
                        stack.append([nr, nc])
    return cnt


def mk_bri():
    for q1 in range(N):
        for q2 in range(M):
            if field[q1][q2] != 0:
                tmp = field[q1][q2]
                for d in range(4):
                    r, c = q1, q2
                    cnt = 0
                    while 0 <= r < N and 0 <= c < M:
                        cnt += 1
                        r, c = r + dr[d], c + dc[d]
                        if not(0 <= r < N and 0 <= c < M):
                            break
                        if field[r][c] == tmp:
                            break
                        elif field[r][c] != 0:
                            if cnt < 3:
                                break
                            if bridge[tmp][field[r][c]] >= cnt:
                                bridge[tmp][field[r][c]] = cnt-1
                                break
                            break


# 세로, 가로
N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
mn = 500
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
num = BFS()
bridge = [[200]*(num+1) for _ in range(num+1)]
mk_bri()
# pprint(field)
# pprint(bridge)
V = num
visited = [0] * (V + 1)
vs = [float('inf')] * (V + 1)
visited[1] = 1
vs[1] = 0
k = 1
cnt = 0
while cnt < V:
    for q in range(V + 1):
        if visited[q] == 0 and bridge[k][q] != 200:
            if bridge[k][q] < vs[q]:
                vs[q] = bridge[k][q]
    mn = float('inf')
    for q in range(V + 1):
        if visited[q] == 0 and vs[q] < mn:
            mn = vs[q]
            k = q
    # print(k, vs)
    visited[k] = 1
    cnt += 1
ans = 0
for q in range(1, V+1):
    if vs[q] != float('inf'):
        ans += vs[q]
    else:
        ans = -1
        break
print(ans)

# final_ans = [200] * (num + 1)
# for k in range(1, num +1):
#     i = k
#     twice = [0] * (num + 1)
#     dist = [200] * (num + 1)
#     dist[i] = 0
#     cnt = 0
#     islands = [[1] for _ in range(num + 1)]
#     while twice != [0]+[1]*num:
#         twice[i] = 1
#         for q in range(1, num+1):
#             if bridge[i][q] != 200:
#                 if bridge[i][q] < dist[q] and twice[q] == 0:
#                     dist[q] = bridge[i][q]
#                     islands[q] = islands[i] + [q]
#         tmp = 200
#         for q in range(1, num+1):
#             if dist[q] < tmp and twice[q] == 0:
#                 tmp = dist[q]
#                 i = q
#         cnt += 1
#         if cnt > num+2:
#             f = 1
#             break
#     # print(dist)
#     for q in range(1, num+1):
#         if final_ans[q] > dist[q] != 0:
#             final_ans[q] = dist[q]
#
# # print(dist)
# # print(islands)
# print(final_ans)
# ans_is = []
# ans = 0
# for q in range(num+1, 1, -1):
#     for q1 in range(2, num+1):
#         if q == len(islands[q1]) and islands[q1][-1] not in ans_is:
#             ans += bridge[islands[q1][-2]][islands[q1][-1]]
#             ans_is.append(islands[q1][-1])
# if len(ans_is) < num-1:
#     ans = -1
# print(ans)