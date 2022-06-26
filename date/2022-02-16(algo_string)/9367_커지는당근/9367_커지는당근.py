# 9367 점점 커지는 당근의 개수
import sys
sys.stdin = open('input_9367.txt')


TC = int(input())
for p in range(TC):
    N = int(input())
    nums = list(map(int, input().split()))

    cnt = 1
    maxs = 1
    for q in range(N-1):
        if nums[q+1] - nums[q] >= 1:
            cnt += 1
            if maxs < cnt:
                maxs = cnt
        else:
            cnt = 1

    print(f'#{p+1} {maxs}')