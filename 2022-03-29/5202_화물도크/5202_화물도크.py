# 5202 화물 도크
import sys
sys.stdin = open('input_5202.txt')

TC = int(input())
for p in range(TC):
    N = int(input())
    working = [list(map(int, input().split())) for _ in range(N)]
    at_time = [0]*25  # 해당 시간에 시작하는 작업
    twice = [0]*25  # 중복되는 시간 확인용

    for q in range(24):
        tmp_mn = 26
        for q1 in range(N):
            if working[q1][0] == q:  # 시작시간이 q 이면,,
                if tmp_mn > working[q1][1]:
                    tmp_mn = working[q1][1]
        if tmp_mn != 26:
            at_time[q] = tmp_mn
    # print(at_time)

    for q in range(24):
        if at_time[q]:
            for q1 in range(q+1, at_time[q]+1):
                if at_time[q1] and at_time[q1] <= at_time[q]:
                    at_time[q] = 0
                    break
    # print(at_time)

    cnt = 0
    for q in range(24):
        if at_time[q]:
            if twice[q] == 0:
                for q1 in range(q, at_time[q]):
                    twice[q1] = 1
                cnt += 1

    print(f'#{p+1} {cnt}')

