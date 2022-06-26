import sys
sys.stdin = open('input_ex1.txt')


def quick(nums, lo, hi):
    if lo < hi:  #
        mid = partition(nums, lo, hi)
        quick(nums, lo, mid-1)
        quick(nums, mid+1, hi)


def partition(nums, lo, hi):
    i = lo-1
    j = lo
    pivot = nums[hi]  # 가장 오른쪽 피벗
    while j < hi:
        if pivot > nums[j]:
            i += 1
            print(f'*{i} {nums[i]} {j} {nums[j]} {nums}')
            if i<j:
                nums[i], nums[j] = nums[j], nums[i]
        j+=1
    nums[i+1], nums[hi] = pivot, nums[i+1]
    print(f'**{i} {nums[i]} {j} {nums[j]} {nums}')
    return i+1


TC = int(input())
for p in range(TC):
    nums = list(map(int, input().split(', ')))
    lo = 0
    hi = len(nums)-1
    quick(nums, lo, hi)
    print(f'#{p+1} {nums}')
