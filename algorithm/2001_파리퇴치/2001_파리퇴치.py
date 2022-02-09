# 2001_파리퇴치
import sys

sys.stdin = open('input_2001.txt')

test_case = int(input())
for p in range(test_case):
    sets = list(map(int, input().split()))
    n = sets[0]
    m = sets[1]

    flies = []

    for q in range(n):
        flies_row = list(map(int, input().split()))  # 파리 열
        flies.append(flies_row)

    dead = 0
    dead_max = 0
    for q1 in range(n - m + 1):

        for q2 in range(n - m + 1):
            dead = 0
            for r1 in range(m):
                for r2 in range(m):
                    dead += flies[q1 + r1][q2 + r2]
                    if dead_max <= dead:
                        dead_max = dead

    print(f'#{p+1} {dead_max}')
