# 5208 전기버스 2
import sys
sys.stdin = open('input_5208.txt')


def bus(energy, cnt, stops, s):
    global mn, N
    if energy < 0 or cnt > mn:
        return
    if s == N:
        if cnt < mn:
            mn = cnt
        return
    bus(energy-1, cnt, stops, s+1)
    bus(stops[s]-1, cnt+1, stops, s+1)


TC = int(input())
for p in range(TC):
    nums = list(map(int, input().split()))
    N = nums[0]
    mn = N
    bus(nums[1], 0, nums, 1)
    print(f'#{p+1} {mn}')
