# 숫자를 정렬하자
import sys
sys.stdin = open('input_1966.txt')

TC = int(input())
for p in range(TC):
    N = int(input())
    nums = list(map(int, input().split()))
    for q1 in range(N - 1):
        for q2 in range(N - q1 -1):
            if nums[q2] > nums[q2 + 1]:
                nums[q2 + 1], nums[q2] = nums[q2], nums[q2 + 1]

    ans = ' '.join(list(map(str, nums)))
    print(f'#{p+1} {ans}')
