# 4875 미로
import sys
import pprint
sys.stdin = open('input_4875.txt')


def DFS(pos):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    global ans

    if mat[pos[0]][pos[1]] == 3:
        ans = 1
        return 0
    mat[pos[0]][pos[1]] = 4
    for q in range(4):
        new_pos = [pos[0] + dr[q], pos[1] + dc[q]]  # 새 위치 탐색
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:
            if mat[new_pos[0]][new_pos[1]] == 0 or mat[new_pos[0]][new_pos[1]] == 3:
                DFS(new_pos)


TC = int(input())

for p in range(TC):

    N = int(input())
    mat = [list(map(int, input())) for _ in range(N)]
    stack = []
    ans = 0
    for q1 in range(N):  # 시작, 끝점 찾아야지
        for q2 in range(N):
            if mat[q1][q2] == 2:
                st = [q1, q2]
            if mat[q1][q2] == 3:
                ed = [q1, q2]
    pos = st
    DFS(pos)
    print(f'#{p+1} {ans}')

