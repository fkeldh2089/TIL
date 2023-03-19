# 23843 콘센트
import sys

sys.stdin = open("input_23843.txt")

from collections import deque
import heapq

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()
ans = 0
q = []
while nums:
    while len(q) < M:
        heapq.heappush(q, nums.pop())
        if nums:
            pass
        else:
            break
    tmp = heapq.heappop(q)
    ans += tmp
    k = 0
    for p in range(len(q)):
        q[p] -= tmp
        if q[p] == 0:
            k += 1
    for p in range(k):
        heapq.heappop(q)

if q:
    ans += max(q)
print(ans)