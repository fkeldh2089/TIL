# Count Unreachable Pairs of Nodes in an Undirected Graph

```python
from collections import deque


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x, y = map(find, (x, y))
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        parent = [i for i in range(n)]

        for s, e in edges:
            if parent[s] != parent[e]:
                union(s, e)
        # print(cnts)
        ans = 0
        cnts = list(Counter(find(k) for k in parent).values())
        return reduce(lambda cnt, x: (cnt[0] + x * cnt[1], cnt[1] + x), cnts, (0, 0))[0]
```

