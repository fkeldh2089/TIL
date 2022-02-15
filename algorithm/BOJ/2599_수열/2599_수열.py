# 2599 수열
import sys
sys.stdin = open('input_2599.txt')

# N은 주어지는 수열 수, K 연속해서 더할 수
N, K = list(map(int, input().split()))
nums = list(map(int, input().split()))

tmp_sum = 0
for q in range(K):  # 일단 시작
    tmp_sum += nums[q]
max_num = tmp_sum
for p in range(N - K):
    tmp_sum -= nums[p]
    tmp_sum += nums[p + K]
    if max_num < tmp_sum:
        max_num = tmp_sum

print(max_num)