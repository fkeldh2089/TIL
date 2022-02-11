# 1961 숫자 배열 회전
import sys
sys.stdin = open('input_1961.txt')

import copy

TC = int(input())

def rot90(n, mat):  # 90 deg 회전
    mat_trans = copy.deepcopy(mat)
    for p1 in range(n):
        for p2 in range(n):
            mat_trans[p2][-p1-1] = mat[p1][p2]

    return mat_trans



for p in range(TC):
    N = int(input())
    mat = []
    for q in range(N):
        col = list(map(int, input().split()))
        mat.append(col)

    fir = rot90(N, mat)  # 90도 회전
    sec = rot90(N, rot90(N, mat))  # 180도 회전
    thr = rot90(N, rot90(N, rot90(N, mat)))  # 270도 회전
    ans = fir + sec + thr


    print(f'#{p+1}')
    for q in range(N):
        for q1 in range(3):
            tmp = ''.join(list(map(str, ans[q + N*q1])))
            print(f'{tmp} ', end='')
        print('')
