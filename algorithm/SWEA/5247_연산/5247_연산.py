# 5247 연산
import sys
sys.stdin = open('input_5247.txt')
from collections import deque

TC = int(input())
for p in range(TC):
    N, M = map(int, input().split())
    cnt = 0
    stack = deque([(N, cnt)])
    visited = set()
    visited.add(N)
    while stack:
        n, cnt = stack.popleft()
        if n + 1 not in visited and n + 1 <= 1000000:
            stack.append((n + 1, cnt + 1))
            visited.add(n + 1)
        if n - 1 not in visited and n - 1 <= 1000000:
            stack.append((n - 1, cnt + 1))
            visited.add(n - 1)
        if n * 2 not in visited and n * 2 <= 1000000:
            stack.append((n * 2, cnt + 1))
            visited.add(n * 2)
        if n - 10 not in visited and n - 10 <= 1000000:
            stack.append((n - 10, cnt + 1))
            visited.add(n - 10)
        if n == M:
            ans = cnt
            break
    print(f'#{p + 1} {ans}')

