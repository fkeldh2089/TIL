# 5102 노드의 거리
import sys
sys.stdin = open('input_5102.txt')


def BFS():
    while stack:
        n = stack.pop(0)
        for p in range(2*E):
            if lines[p][0] == n and twice[lines[p][1]] == 0:
                stack.append(lines[p][1])
                twice[lines[p][1]] = twice[lines[p][0]] + 1


TC = int(input())

for p in range(TC):
    V, E = map(int, input().split())
    lines = []
    for q in range(E):
        line1 = list(map(int, input().split()))
        line2 = [line1[1], line1[0]]
        lines.append(line1)
        lines.append(line2)
    S, G = map(int, input().split())
    stack = [S]
    twice = [0] * (V+1)
    twice[S] = 1
    BFS()
    if twice[G] == 0:
        twice[G] = 1
    print(f'#{p+1} {twice[G]-1}')