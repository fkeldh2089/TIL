# Reorder Routes to Make All Paths Lead to the City Zero

```python
from collections import deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        ans = 0
        for p in range(len(connections)):
            s, e = connections[p]
            graph[s].append([e, 1])
            graph[e].append([s, -1])
        
        q = deque()
        q.append(0)
        visited = [0]*n
        visited[0] = 1
        while q:
            cur = q.pop()
            # print(cur)
            for p in range(len(graph[cur])):
                nx, dr = graph[cur][p]
                # print(nx, dr)
                if visited[nx] == 0:
                    visited[nx] = 1
                    if dr == 1:
                        ans += 1
                    else:
                        pass
                    q.appendleft(nx)
            # print(q)

        return ans
```

