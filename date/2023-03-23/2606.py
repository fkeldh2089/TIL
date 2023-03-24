# 2606 바이러스
import sys
sys.stdin = open("input_2606.txt")

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
answer = 0
for p in range((m)):
    connection = list(map(int, input().split()))
    a = connection[0]
    b = connection[1]
    graph[a].append(b)
    graph[b].append(a)
def bfs(n):
    for p in graph[n]:
        if visited[p] == 0:
            visited[p] = 1
            bfs(p)

answer = answer + 1
visited[1] = 1
bfs(1)
print(sum(visited)-1)