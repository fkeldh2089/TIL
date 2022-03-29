# 1249 보급로
import sys

sys.stdin = open('input_1249.txt')

# visited만을 사용하여 시간 및 방문 여부를 확인하려 하였는데,,, 시간이 0인 구간이
# 있어 알고리즘이 꼬여버린다.

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
                    visited[nr][nc] = visited[r][c] + mat[nr][nc]
                    twice[nr][nc] = 1
                    stack.append((nr, nc))
                else:
                    if visited[nr][nc] > visited[r][c] + mat[nr][nc]:
                        visited[nr][nc] = visited[r][c] + mat[nr][nc]
                        stack.append([nr, nc])

TC = int(input())
for p in range(TC):
    N = int(input())
    mat = [list(map(int, list(input()))) for _ in range(N)]
    mn = 0
    for q in range(N):
        mn += mat[0][q] + mat[q][-1]
    visited = [[0] * N for _ in range(N)]
    twice = [[0] * N for _ in range(N)]
    twice[0][0] = 1
    minsum(0, 0, visited, twice)
    print(f'#{p+1} {visited[-1][-1]}')
