# 5204 병합 정렬
import sys
sys.stdin = open('input_5204.txt')
from collections import deque

def merge(left, right):
    global cnt
    result = [0] * (len(left)+len(right))
    i = 0
    i1 = 0
    i2 = 0
    if left[-1] > right[-1]:
        cnt += 1
    while len(left) > i1 or len(right) > i2:
        if len(left) > i1 and len(right) > i2:
            if left[i1] <= right[i2]:
                result[i] = left[i1]
                i += 1
                i1 += 1
            else:
                result[i] = right[i2]
                i += 1
                i2 += 1

        elif len(left) > i1:
            result[i] = left[i1]
            i += 1
            i1 += 1
        elif len(right) > i2:
            result[i] = right[i2]
            i += 1
            i2 += 1
    return result


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)


TC = int(input())
for p in range(TC):
    cnt = 0
    N = int(input())
    nums = list(map(int, input().split()))
    ans = merge_sort(nums)
    print(f'#{p+1} {ans[N // 2]} {cnt}')
