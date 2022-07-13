# 1135 뉴스 전하기
import sys
from collections import defaultdict, deque
sys.stdin = open('input_1135.txt')


def searchtree(n):
    global mn
    if n == -1:
        return 0
    else:
        weight[n] += 1
        searchtree(nodeinfo[n])



N = int(input())
nodeinfo = list(map(int, input().split()))
node = defaultdict(list)
L = len(nodeinfo)  # 노드의 자손 갯수
weight = [0] * L  #
directchild = [0] * L
mn = 0
f = 0
for p in range(1, L):
    searchtree(p)
    directchild[nodeinfo[p]] += 1
for p in range(1, L):
    node[nodeinfo[p]].append((weight[p], p))
for idx, value in node.items():
    value.sort()
    node[idx]=value
cnt = 0
stack = deque()
stack.append(0)
while stack:
    i = len(stack)
    for p in range(i):
        tmp = stack.popleft()
        if node[tmp]:
            w, n = node[tmp].pop()
            stack.append(tmp)
            stack.append(n)
    cnt += 1

print(cnt-1)