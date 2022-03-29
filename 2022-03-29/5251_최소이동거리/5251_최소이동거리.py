# 5251 최소 이동 거리
import sys
from pprint import pprint
sys.stdin = open('input_5251.txt')


TC = int(input())
for p in range(TC):
    N, E = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(E)]
    dist = [[1000000]*(N+1) for _ in range(N+1)]
    for q in range(E):
        dist[roads[q][0]][roads[q][1]] = roads[q][2]

    cnt = [100000]*(N+1)
    cnt[0] = 0
    twice = [0]*(N+1)
    while twice != [1]*(N+1):
        mn = 1000000
        for q in range(N+1):
            if twice[q] == 0 and cnt[q] < mn:
                mn = cnt[q]
                node = q

        twice[node] = 1
        for q in range(N+1):
            if cnt[q] > dist[node][q] + cnt[node]:
                cnt[q] = dist[node][q] + cnt[node]

    print(f'#{p+1} {cnt[-1]}')