# Number of Operations to Make Network Connected

```python
from collections import defaultdict
import sys

# sys.setrecursionlimit(10**6)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1:
            return -1

        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        answer = 0
        for connection in connections:
            a = connection[0]
            b = connection[1]
            graph[a].append(b)
            graph[b].append(a)
        def bfs(n):
            for p in graph[n]:
                if visited[p] == 0:
                    visited[p] = 1
                    bfs(p)
        
        for i in range(n):
            if visited[i] == 0:
                answer = answer + 1
                visited[i] = 1
                bfs(i)
        
        return answer - 1
```

