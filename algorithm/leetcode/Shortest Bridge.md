# Shortest Bridge

```python
from collections import deque
from pprint import pprint

class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        answer = 10000
        def findIsl():
            for p1 in range(len(grid)):
                for p2 in range(len(grid[0])):
                    if grid[p1][p2]:
                        return [p1, p2]
        
        sr, sc = findIsl()
        grid[sr][sc] = -1
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        q = deque()
        q2 = deque()
        q.append([sr, sc])
        q2.append([sr, sc])
        while q2:
            r, c = q2.pop()
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0<=nr and nr< len(grid) and 0<=nc and nc<len(grid[0]):
                    if grid[nr][nc] == 1:
                        q2.append([nr, nc])
                        q.append([nr, nc])
                        grid[nr][nc] = -1      

        # pprint(grid)

        while q:
            r, c = q.pop()
            for d in range(4):
                nr, nc = r+dr[d], c+dc[d]
                if 0<=nr and nr< len(grid) and 0<=nc and nc<len(grid[0]):
                    if grid[nr][nc] == 1:
                        if answer > -grid[r][c]:
                            answer = -grid[r][c]
                    else:
                        if grid[nr][nc] == 0 or grid[nr][nc] < grid[r][c] -1:
                            grid[nr][nc] = grid[r][c] -1
                            q.appendleft([nr, nc])
        # pprint(grid)
        return answer-1
```

