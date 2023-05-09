# Matrix Diagonal Sum

```python
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for p in range(len(mat)):
            ans += mat[p][p]
            ans += mat[len(mat)-1-p][p]
        if len(mat)%2:
            ans -= mat[len(mat)//2][len(mat)//2]
        return ans
```

