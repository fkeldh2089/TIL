# 1209_Sum
import sys

sys.stdin = open('input_1209.txt')

for p in range(10):
    tc = int(input())
    mat = []

    for q in range(100):
        mrow = list(map(int, input().split()))  # 열
        mat.append(mrow)

    sum_max = 0
    for q1 in range(100):
        sum_row = 0
        sum_col = 0
        for q2 in range(100):
            sum_row += mat[q1][q2]
            sum_col += mat[q2][q1]
            if sum_max <= sum_row:
                sum_max = sum_row
            if sum_max <= sum_col:
                sum_max = sum_col

    sum_cro1 = 0
    sum_cro2 = 0
    for q in range(100):
        sum_cro1 += mat[q][q]
        sum_cro2 += mat[-1 - q][-1 - q]

    if sum_max <= sum_cro1:
        sum_max = sum_cro1
    if sum_max <= sum_cro2:
        sum_max = sum_cro2

    print(f'#{p + 1} {sum_max}')