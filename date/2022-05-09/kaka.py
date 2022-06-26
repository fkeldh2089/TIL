from collections import deque

def solution(n, start, end, roads, traps):
    answer = 0
    dis1 = [[0]*(n+1) for _ in range(n+1)]
    dis2 = [[0]*(n+1) for _ in range(n+1)]
    dis = [0, dis1, dis2]
    visited = [[0, -1, -1] for _ in range(n+1)]

    for s, e, d in roads:
        dis1[s][e] = d  # 원래 진행 방향
        dis2[e][s] = e  # 역 방향


    return answer


def BFS(num, visited, n, dis):
    stack = deque()
    stack.append(num)
    f = 1
    visited[num][f] = 1
    while stack:
        n = stack.popleft()
        for p in range(n):
            if visited[p][f] != dis[f][n][p] != 0