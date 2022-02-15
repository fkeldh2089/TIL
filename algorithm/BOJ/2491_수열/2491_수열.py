# 2491 수열
import sys
sys.stdin = open('input_2491.txt')

N = int(input())  # 수열
numbers = list(map(int, input().split()))  # 수열

# 올라갈때는 1, 내려갈때는 2 - 시간 초과

ans = 1
cnt = 1
for p in range(N-1):
    if numbers[p] <= numbers[p+1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

cnt = 1
for p in range(N-1):
    if numbers[p] >= numbers[p+1]:
        cnt += 1
    else:
        cnt = 1
    if ans < cnt:
        ans = cnt

print(ans)
# ans = 0
# for p in range(N-1):
#     cnt = 1
#     if numbers[p] <= numbers[p+1]:
#         while p + cnt + 1 < N and numbers[p + cnt] <= numbers[p + cnt + 1]:
#             cnt += 1
#         if cnt > ans:
#             ans = cnt
#     cnt = 1
#     if numbers[p] >= numbers[p+1]:
#         while p + cnt + 1 < N and numbers[p + cnt] >= numbers[p + cnt + 1]:
#             cnt += 1
#         if cnt > ans:
#             ans = cnt
#
# print(ans + 1)