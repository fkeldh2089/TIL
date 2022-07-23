# 17182_우주 탐사선
import sys
sys.stdin = open('input_17182.txt')


def DFS(s, cnt, k):
    global mn, N
    if k<N:
        for p in range(N):
            if visited[p]:
                visited[p] = 0
                DFS(p, cnt + short[s][p], k+1)
                visited[p] = 1
    else:
        if cnt < mn:
            mn = cnt


def FW():
    sdist = [[float('inf')]*N for _ in range(N)]
    for p in range(N):
        for q in range(N):
            sdist[p][q] = dist[p][q]

    for p1 in range(N):
        for p2 in range(N):
            for p3 in range(N):
                if sdist[p2][p3] > sdist[p2][p1] + sdist[p1][p3]:
                    sdist[p2][p3] = sdist[p2][p1] + sdist[p1][p3]
    return sdist

N, K = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(N)]
mn = float('inf')
short = FW()
print(short)
visited = [1] * N
DFS(K, 0, 0)
print(mn)
