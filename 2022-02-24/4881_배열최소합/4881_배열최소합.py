# 4881 배열 최소 합
import sys
import pprint
sys.stdin = open('input_4881.txt')


def mn_sum(N, mat, i, visited, tmp):
    global min_num
    if i == N:
        if tmp < min_num:
            min_num = tmp
        return 0

    if tmp > min_num:
        return 0

    for p in range(N):
        if visited[p] == 0:
            tmp += mat[i][p]
            visited[p] = 1
            mn_sum(N, mat, i+1, visited, tmp)
            visited[p] = 0
            tmp -= mat[i][p]


TC = int(input())

for p in range(TC):
    N = int(input())  # N by N
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_num = 40
    tmp = 0
    mn_sum(N, mat, 0, visited, 0)
    print(f'#{p+1} {min_num}')

