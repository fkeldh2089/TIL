# 2309 일곱 난쟁이
import sys
sys.stdin = open('input_2309.txt')


def find_hobbit(de_sum, tall):
    for p1 in range(9):
        tall_sum1 = 0
        tall_tmp1 = tall[::]
        tall_sum1 += tall_tmp1.pop(p1)
        for p2 in range(8):
            tall_sum2 = tall_sum1
            tall_tmp2 = tall_tmp1[::]
            tall_sum2 += tall_tmp2.pop(p2)
            if tall_sum2 == de_sum - 100:
                return tall_tmp2


def sort_pill(N, nums):  # 버블 소트
    for q1 in range(N - 1):
        for q2 in range(N - q1 - 1):
            if nums[q2] > nums[q2 + 1]:
                nums[q2 + 1], nums[q2] = nums[q2], nums[q2 + 1]
    return nums


tall = []
de_sum = 0
for p in range(9):
    N = int(input())
    tall.append(N)
    de_sum += N

ans = find_hobbit(de_sum, tall)
ans = sort_pill(7, ans)
for p in range(7):
    print(ans[p])

