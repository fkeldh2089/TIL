import sys
from collections import defaultdict
sys.stdin = open('input_1800.txt')


# N 학생 번호, P 케이블 개수, K 공짜 케이블
N, P, K = map(int, input().split())

costs = [[0]*(N+1) for _ in range(N+1)]
visited = [1000000000000]*(N+1)


for p in range(P):
    s, e, c = map(int, input().split())
    costs[s][e] = c
    costs[e][s] = c

stack = [[1, 0]]
while stack:
    s, cnt = stack.pop(0)
    for p in range(N+1):
        if costs[s][p]:
            if visited[p] > costs[s][p] + cnt:
                visited[p] = costs[s][p] + cnt
                stack.append([p, costs[s][p] + cnt])
    print(visited)
    print(stack)
print(visited[N])