# 5178 노드의 합
import sys
sys.stdin = open('input_5178.txt')


def rnode(n):
    if nodes[n] == 0:
        rnode(2* n)
        if n*2 + 1 <= N:
            rnode(2*n + 1)
            nodes[n] = nodes[n*2] + nodes[n*2 + 1]
        elif n*2 <= N:
            nodes[n] = nodes[n*2]
    else:
        pass

TC = int(input())

for p in range(TC):
    N, M, L = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(M)]

    li1 = [0] * N
    li2 = [0] * N
    nodes = [0] * (N + 1)

    for q in range(M):
        # if li1[nums[q][0]] == 0:
        #     li1[nums[q][0]] = nums[q][1]
        # else:
        #     li2[nums[q][0]] = nums[q][1]
        nodes[nums[q][0]] = nums[q][1]
    rnode(L)
    print(f'#{p+1} {nodes[L]}')
