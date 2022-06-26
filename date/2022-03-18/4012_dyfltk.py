# 4012 요리사
import sys
from pprint import pprint
sys.stdin = open('input_4012.txt')


def reci(nums, nums1):
    global N, syn, mn
    l = len(nums)
    # print(nums, nums1)
    if l*2 == N:
        cnt1 = 0
        for p1 in range(l):
            for p2 in range(l):
                cnt1 += syn[nums[p1]][nums[p2]]
        cnt2 = 0
        for p1 in range(l):
            for p2 in range(l):
                cnt2 += syn[nums1[p1]][nums1[p2]]
        tmp = abs(cnt2 - cnt1)
        if tmp < mn:
            mn =tmp
        # print(tmp)
        return
    if nums[0] == N//2 -1:
        return
    for p in range(l):
        nums1.append(nums[p])
        tmp_nums = nums[0:p]+nums[p+1:]
        reci(tmp_nums, nums1)
        nums1.pop()


def DFS(n, alst, blst):
    global ans
    if n == N:
        if len(alst) == len(blst):
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum - bsum):
                ans = abs(asum - bsum)
        return

    DFS(n + 1, alst + [n], blst)
    DFS(n + 1, alst, blst + [n])



TC = int(input())

for p in range(TC):
    N = int(input())
    syn = [list(map(int, input().split())) for _ in range(N)]
    arr =syn
    mn = 100000
    ans = 123123456
    nums = list(range(N))
    # reci(nums, [])
    DFS(0, [], [])
    print(f'#{p+1} {ans}')
