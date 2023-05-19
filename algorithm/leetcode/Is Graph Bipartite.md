# Is Graph Bipartite

```python
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        q = deque()
        visited = [0]*len(graph)
        for p in range(len(graph)):
            if visited[p] == 0:
                q.append(p)
                visited[p] = 1
                while q:
                    cur = q.pop()
                    # print(cur)
                    # print(visited)
                    f = visited[cur]
                    for node in graph[cur]:
                        if visited[node]:
                            if visited[node] == f:
                                return False
                        else:
                            visited[node] = -f
                            q.appendleft(node)
        return True
```

