import sys
from pprint import pprint
sys.stdin = open('inputt.txt')
sys.setrecursionlimit(10000)


def DFS(r, c):
    global ans
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0<=nr<100 and 0 <=nc<100 and visited[nr][nc] == 0 and field[nr][nc] != 1:
            if field[nr][nc] == 3:
                ans = 1
            visited[nr][nc] = 1
            DFS(nr, nc)


def DFS1(r, c):
    global ans
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while 1:
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 100 and 0 <= nc < 100 and visited[nr][nc] == 0 and field[nr][nc] != 1:
                if field[nr][nc] == 3:
                    ans = 1
                    return
                visited[nr][nc] = 1
                stack.append([r, c])
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                return


for p in range(10):
    N = int(input())
    field = [list(map(int, list(input()))) for _ in range(100)]
    visited = [[0]*100 for _ in range(100)]
    ans = 0
    stack = []

    for q1 in range(100):
        for q2 in range(100):
            if field[q1][q2] == 2:
                sr, sc = q1, q2
    visited[sr][sc] = 1
    # print(sr, sc)
    DFS1(sr, sc)

    print(f'#{p+1} {ans}')