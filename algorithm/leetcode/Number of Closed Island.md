# Number of Closed Island

```python
from collections import deque
from pprint import pprint

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        ans = 0
        visited = [[0]*m for _ in range(n)]
        for p1 in range(n):
            for p2 in range(m):
                if grid[p1][p2] == 0:
                    if visited[p1][p2] == 0:
                        q = deque()
                        q.append([p1, p2])
                        visited[p1][p2] = 1
                        f = 0
                        while q:
                            r, c = q.pop()
                            if r == 0 or r == n-1 or c==0 or c==m-1:
                                f = 1
                            for d in range(4):
                                nr, nc = r+dr[d], c+dc[d]
                                if 0<=nr and nr<=n-1 and 0<=nc and nc<=m-1:
                                    if visited[nr][nc] == 0 and grid[nr][nc]==0:
                                        q.appendleft([nr,nc])
                                        visited[nr][nc] = 1
                        
                        if f==0:
                            ans += 1
        return ans
```

