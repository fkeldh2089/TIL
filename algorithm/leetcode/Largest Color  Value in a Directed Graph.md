# Largest Color  Value in a Directed Graph

```python
from collections import defaultdict,deque


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        ans = 0
        processed = 0
        gra = defaultdict(list)
        visited = [0] * n
        q = deque()
        count = [[0] * 26 for _ in range(n)]

        for s, e in edges:
            gra[s].append(e)
            visited[e] += 1
        for p in range(len(visited)):
            if visited[p] == 0:
                q.append(p)

        while q:
            cur = q.pop()
            processed += 1
            count[cur][ord(colors[cur]) - ord('a')] += 1
            ans = max(ans, count[cur][ord(colors[cur]) - ord('a')])
            for e in gra[cur]:
                for p in range(26):
                    count[e][p] = max(count[e][p], count[cur][p])
                visited[e] -= 1
                if visited[e] == 0:
                    q.appendleft(e)

        return ans if processed == n else -1
```

