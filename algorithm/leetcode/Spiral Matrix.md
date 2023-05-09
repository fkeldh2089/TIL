# Spiral Matrix

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        ans = []
        r, c = 0 ,0
        d = 0
        ans.append(matrix[r][c])
        visited[r][c] = 1
        while len(ans) < len(matrix)*len(matrix[0]):
            nr, nc = r+dr[d], c+dc[d]
            if 0<=nr and nr<len(matrix) and 0<=nc and nc<len(matrix[0]) and visited[nr][nc]==0:
                r, c = nr, nc
                ans.append(matrix[r][c])
                visited[r][c] = 1
            else:
                d = (d+1)%4
        
        return ans
```

