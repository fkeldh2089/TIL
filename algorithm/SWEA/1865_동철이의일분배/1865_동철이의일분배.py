# 1865 동철이의 일 분배
import sys
sys.stdin = open('input_1865.txt')
from itertools import permutations


def DFS(ans, n):
    global mn, visited
    if ans <= mn:
        return
    if n == N:
        if ans > mn:
            mn = ans

    for q in range(N):
        if visited[q] == 0:
            visited[q] = 1
            DFS(ans*(mat[n][q]/100), n+1)
            visited[q] = 0


TC = int(input())
for p in range(TC):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    mn = 0
    visited = [0]*N
    DFS(1, 0)
    print(f'#{p+1} {mn*100:.6f}')