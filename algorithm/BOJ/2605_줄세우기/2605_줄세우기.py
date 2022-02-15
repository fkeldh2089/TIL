# 2605 줄 세우기
import sys
sys.stdin = open('input_2605.txt')

N = int(input())
line = [p for p in range(1, N+1)]  # 일단 베이스 줄
nums = list(map(int, input().split()))  # 뽑은 번호
new_line = []
for p in range(N):
    line = line[0:p-nums[p]] + line[p:p+1] + line[p-nums[p]:p] + line[p+1:]

print(*line)