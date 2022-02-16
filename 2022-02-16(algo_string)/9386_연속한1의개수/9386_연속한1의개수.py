# 9386 연속한 1의 개수
import sys
sys.stdin = open('input_9386.txt')


TC = int(input())
for p in range(TC):
    N = int(input())
    nums = input()

    maxs = 0
    cnt = 0
    for q in range(N):
        if nums[q] == '1':
            cnt += 1
            if maxs < cnt:
                maxs= cnt
        else:
            cnt = 0

    print(f'#{p+1} {maxs}')
