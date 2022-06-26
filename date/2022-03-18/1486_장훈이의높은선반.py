# 1486 장훈이의 높은 선반
import sys
from pprint import pprint
sys.stdin = open('input_1486.txt')
from copy import deepcopy


def talls(nums, cnt):
    global mn
    if cnt >= H:
        if mn > cnt-H:
            mn = cnt -H
    l = len(nums)
    for q in range(l):
        cnt += nums[q]
        tmp_nums = nums[q+1:]
        talls(tmp_nums, cnt)
        cnt -= nums[q]


TC = int(input())
for p in range(TC):
    N, H = map(int, input().split())
    nums = list(map(int, input().split()))
    mn = 5000
    talls(nums, 0)
    print(f'#{p+1} {mn}')
