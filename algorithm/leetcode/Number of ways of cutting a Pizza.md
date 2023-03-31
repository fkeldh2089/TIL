# Number of ways of cutting a Pizza

```python
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        @cache
        def dfs(i, j, k):
            if k == 0:
                return int(dp[-1][-1] - dp[-1][j] - dp[i][-1] + dp[i][j] > 0)
            res = 0
            for x in range(i + 1, m):
                if dp[x][-1] - dp[x][j] - dp[i][-1] + dp[i][j]:
                    res += dfs(x, j, k - 1)
            for y in range(j + 1, n):
                if dp[-1][y] - dp[-1][j] - dp[i][y] + dp[i][j]:
                    res += dfs(i, y, k - 1)
            return res % mod

        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for r, row in enumerate(pizza):
            for c, v in enumerate(row):
                dp[r + 1][c + 1] = dp[r + 1][c] + dp[r][c + 1] - dp[r][c] + int(v == 'A')
        print(dp)
        return dfs(0, 0, k - 1)
```

