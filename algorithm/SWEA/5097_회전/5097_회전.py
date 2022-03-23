# 5097 회전
import sys
sys.stdin = open('input_5097.txt')

TC = int(input())

for p in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for q in range(M):
        tmp = nums.pop(0)
        nums.append(tmp)

    print(f'#{p+1} {nums[0]}')