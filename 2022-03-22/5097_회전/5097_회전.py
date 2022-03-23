# 5097 회전
import sys
from collections import deque
sys.stdin = open('input_5097.txt')

TC = int(input())

for p in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    nums2 = deque(nums[::])

    for q in range(M):
        tmp = nums.pop(0)
        nums.append(tmp)

    nums2.rotate(-M)
    print(f'#{p+1} {nums[0]} {nums2[0]}')