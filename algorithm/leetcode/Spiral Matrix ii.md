# Spiral Matrix ii

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        ans = [[0]*n for _ in range(n)]
        
        r, c = 0, 0
        ans[0][0] = 1
        d = 0
        cnt = 1
        while cnt < n**2:
            nr ,nc = r+dr[d], c+dc[d]
            if 0<=nr and nr<n and 0<=nc and nc<n and ans[nr][nc] == 0:
                ans[nr][nc] = ans[r][c] + 1
                r, c = nr, nc
                cnt += 1
            else:
                d += 1
                d %= 4
        return ans
```

