# 5249 최소 신장 트리
import sys
sys.stdin = open('input_5429.txt')


TC = int(input())
for p in range(TC):
    V, E = map(int, input().split())
    lines = [list(map(int, input().split())) for _ in range(E)]
    dist = [[0]*(V+1) for _ in range(V+1)]
    for q in range(E):
        dist[lines[q][0]][lines[q][1]] = lines[q][2]
        dist[lines[q][1]][lines[q][0]] = lines[q][2]
    visited = [0]*(V+1)
    vs = [float('inf')]*(V+1)
    visited[0] = 1
    vs[0] = 0
    k = 0
    cnt = 0
    while cnt < V:
        for q in range(V+1):
            if visited[q] == 0 and dist[k][q] != 0:
                if dist[k][q] < vs[q]:
                    vs[q] = dist[k][q]
        mn = float('inf')
        for q in range(V+1):
            if visited[q] == 0 and vs[q] < mn:
                mn = vs[q]
                k = q
        print(k, vs)
        visited[k] = 1
        cnt += 1
    print(f'#{p+1} {sum(vs)}')