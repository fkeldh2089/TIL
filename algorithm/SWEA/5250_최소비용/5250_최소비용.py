# 5250 최소 비용
import sys
from pprint import pprint
sys.stdin = open('input_5250.txt')


def minsum(r, c, visited, twice):
    stack = [[r, c]]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while stack:
        r, c = stack.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and nr+nc != 0:
                if visited[nr][nc] == 0 and twice[nr][nc] == 0:
                    if mat[r][c] - mat[nr][nc] >= 0:
                        visited[nr][nc] = visited[r][c] + 1
                    else:
                        visited[nr][nc] = visited[r][c] + mat[nr][nc]-mat[r][c] + 1
                    twice[nr][nc] = 1
                    stack.append((nr, nc))
                    # pprint(visited)
                else:
                    if mat[r][c] - mat[nr][nc] >= 0:
                        tmp = visited[r][c] + 1
                    else:
                        tmp = visited[r][c] + mat[nr][nc]-mat[r][c] + 1
                    if visited[nr][nc] > tmp:
                        visited[nr][nc] = tmp
                        stack.append([nr, nc])

TC = int(input())
for p in range(TC):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    mn = 0
    for q in range(N):
        mn += mat[0][q] + mat[q][-1]
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    twice = [[0] * N for _ in range(N)]
    twice[0][0] = 1
    minsum(0, 0, visited, twice)
    print(f'#{p+1} {visited[-1][-1]-1}')
