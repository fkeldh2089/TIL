# 4861 회문
import sys
sys.stdin = open('input_4861.txt')

TC = int(input())

for p in range(TC):
    # N개의 글자를 가진 N개의 줄, M 길이의 회문 길이
    N, M = list(map(int, input().split()))
    mat = [input() for _ in range(N)]
    mat2 =[]

    for q1 in range(N):
        tmp = ''
        for q2 in range(N):
            tmp += mat[q2][q1]
        mat2.append(tmp)

    ans = ''
    for q1 in range(N):
        tmp = ''
        for q2 in range(N - M + 1):
            tmp1 = mat[q1][q2:q2+M]
            tmp2 = mat2[q1][q2:q2+M]
            if tmp1 == tmp1[::-1]:
                ans = tmp1
                break
            if tmp2 == tmp2[::-1]:
                ans = tmp2
                break

    print(f'#{p+1} {ans}')
