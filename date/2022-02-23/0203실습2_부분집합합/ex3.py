# ex3 부분 집합의 합
import sys
# sys.stdin = open('input_ex2.txt')

mat = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = [0] * 10
ans = []
col = []
for q1 in range(1 << 10):
    tmp = 0
    col = []
    for q2 in range(10):
        if q1 & (1 << q2):
            tmp += mat[q2]
            col.append(mat[q2])
    if tmp == 10:
        ans.append(col)
print(ans)