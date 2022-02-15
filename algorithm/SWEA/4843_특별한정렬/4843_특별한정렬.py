# 4843 특별한 정렬
import sys
sys.stdin = open('input_4843.txt')

TC = int(input())
for p in range(TC):
    N = int(input())
    nums = list(map(int, input().split()))

    for q in range(N):
        tmp_index = q
        for q1 in range(q, N):
            if q%2:
                if nums[tmp_index] > nums[q1]:
                    tmp_index = q1
            else:
                if nums[tmp_index] < nums[q1]:
                    tmp_index = q1
        nums[tmp_index], nums[q] = nums[q], nums[tmp_index]

    ans = ' '.join(map(str, nums[0:10]))
    print(f'#{p+1} {ans}')
