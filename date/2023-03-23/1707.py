# 1707 이분 그래프
import sys
sys.stdin = open("input_1707.txt")


from collections import deque


K = int(input())


for k in range(K):
    n, E = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for p in range(E):
        connection = list(map(int, input().split()))
        a = connection[0]
        b = connection[1]
        graph[a].append(b)
        graph[b].append(a)

    f = 1
    for p in range(1, n+1):
        if visited[p] == 0:
            q = deque()
            visited[p] = 1
            q.append([p, 1])
            # print(q)
            # print(graph)
            # print(visited)
            while q:
                cur, cn = q.pop()
                for p1 in range(len(graph[cur])):
                    if visited[graph[cur][p1]]:
                        if visited[graph[cur][p1]] == cn:
                            f = 0
                        else:
                            pass
                    else:
                        visited[graph[cur][p1]] = 3-cn
                        q.appendleft([graph[cur][p1], 3-cn])
                # print(q)
                # print(visited)
    if f:
        print('YES')
    else:
        print('NO')