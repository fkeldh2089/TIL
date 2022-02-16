# 9489 고대유적
import sys
sys.stdin = open('input_9489.txt')


TC = int(input())
for p in range(TC):
    W, H = list(map(int, input().split()))
    nums = [list(map(int, input().split())) for _ in range(W)]

    maxs = 0

    for q1 in range(W):
        cnt1 = 0
        for q2 in range(H):
            if nums[q1][q2] == 1:
                cnt1 += 1
                if maxs < cnt1:
                    maxs = cnt1
            else:
                cnt1 = 0
    for q1 in range(H):
        cnt1 = 0
        for q2 in range(W):
            if nums[q2][q1] == 1:
                cnt1 += 1
                if maxs < cnt1:
                    maxs = cnt1
            else:
                cnt1 = 0


    print(f'#{p+1} {maxs}')
