# 6198 옥상 정원 꾸미기
import sys
sys.stdin = open("input_6198.txt")


import heapq

N = int(input())
q = []
ans = 0
for p in range(N):
    cur = int(input())
    while q and cur >= q[0]:
        heapq.heappop(q)
    ans += len(q)
    heapq.heappush(q, cur)
print(ans)