# Minimum Path Sum

```python
from collections import deque


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = [[-1]*len(grid[0]) for _ in range(len(grid))]
        visited[0][0] = grid[0][0]
        q= deque()
        q.append([0, 0])

        dr = [0, 1]
        dc = [1, 0]
        while q:
            r, c = q.pop()
            for d in range(2):
                nr, nc = r + dr[d], c + dc[d]
                if 0<=nr and nr < len(grid):
                    if 0<=nc and nc<len(grid[0]):
                        if visited[nr][nc] == -1:
                            visited[nr][nc] = visited[r][c] + grid[nr][nc]
                            q.appendleft([nr, nc])
                        elif visited[nr][nc] > visited[r][c] + grid[nr][nc]:
                            visited[nr][nc] = visited[r][c] + grid[nr][nc]
                            q.appendleft([nr, nc])
        return visited[-1][-1]
```

