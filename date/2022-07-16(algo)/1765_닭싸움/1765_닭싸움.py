# 1765 닭싸움 팀 정하기
import sys
from collections import defaultdict
sys.stdin = open('input_1765.txt')
sys.setrecursionlimit(10**9)


def team(n):
    if Friend[n]==0:
        return n
    Friend[n] = team(Friend[n])
    return Friend[n]


N = int(input())
M = int(input())

Enemy = [[] for _ in range(N+1)]
Friend = [0]*(N+1)
cnt = 0

for p in range(M):
    S, n1, n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    if S == 'E':
        Enemy[n1].append(n2)
        Enemy[n2].append(n1)
    else:
        m1 = team(n1)
        m2 = team(n2)
        if m1 != m2:
            Friend[m2] = m1

for value in Enemy:
    for p in range(1, len(value)):
        m1 = team(value[0])
        m2 = team(value[p])
        if m1 != m2:
            Friend[m2] = m1

for p in range(1, N+1):
    if Friend[p]:
        pass
    else:
        cnt += 1

print(cnt)