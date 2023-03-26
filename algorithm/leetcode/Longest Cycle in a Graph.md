# Longest Cycle in a Graph

```python
from collections import defaultdict


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        ans = -1
        for p in range(len(edges)):
            if edges[p] != -1:
                visited = defaultdict(lambda : -1)
                # print(p)
                visited[p] = 0
                cur = p
                while 1:
                    # print(cur)
                    if edges[cur] != -1:
                        nx = edges[cur]
                        edges[cur] = -1
                        if visited[nx]!=-1:
                            # print(11, q)
                            a = visited[cur]-visited[nx]+1
                            if a>ans:
                                ans = a
                        visited[nx] = visited[cur]+1
                        cur = nx
                    else:
                        break
        
        return ans

```

