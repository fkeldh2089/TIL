# 5248 그룹 나누기
import sys
sys.stdin = open('input_5248.txt')


TC = int(input())
for p in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    twice = [0]*(N+1)
    dist = [[0]*(N+1) for _ in range(N+1)]
    for q in range(M):
        dist[nums[2*q]][nums[2*q+1]] = 1
        dist[nums[2*q+1]][nums[2*q]] = 1

    cnt = -1
    for q in range(N+1):
        stack = []
        if twice[q] == 0:
            stack.append(q)
            cnt += 1
        while stack:
            st = stack.pop(0)
            for q1 in range(N+1):
                if dist[st][q1] and twice[q1] == 0:
                    twice[q1] = 1
                    stack.append(q1)
        # print(q, twice, cnt)
    print(f'#{p+1} {cnt}')

