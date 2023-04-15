# Maximum Value of k Coins From Piles

```python
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @cache
        def dp(i: int, k: int) -> int:
            if i == len(piles) or k == 0:
                return 0
            ans = dp(i + 1, k)
            val = 0

            for j in range(min(len(piles[i]), k)):
                val += piles[i][j]
                ans = max(ans, val + dp(i + 1, k - j - 1))

            return ans

        return dp(0, k)
```

