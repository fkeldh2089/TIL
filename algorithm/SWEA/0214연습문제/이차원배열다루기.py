# 연습문제 1 이차원 배열 다루기
import sys
sys.stdin = open('input_ex1.txt')

TC = int(input())
for p in range(TC):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    dir = [1, -1]
    sum_tmp = 0
    for q1 in range(N):
        for q2 in range(N):
            for r in range(2):
                if 0 <= q2 + dir[r] < N:
                    tmp = nums[q1][q2] - nums[q1][q2 + dir[r]]
                    if tmp < 0:
                        tmp = tmp * (-1)
                    sum_tmp += tmp
                if 0 <= q1 + dir[r] < N:
                    tmp = nums[q1][q2] - nums[q1 + dir[r]][q2]
                    if tmp < 0:
                        tmp = tmp * (-1)
                    sum_tmp += tmp

    print(f'#{p+1} {sum_tmp}')
