# Count Ways to Build Good Strings

```python
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)
        dp[0] = 1
        mod = 10**9+7
        for p in range(len(dp)):
            n1 = p+zero
            n2 = p+one
            if n1 <= high:
                dp[n1] += dp[p] %mod
            if n2 <= high:
                dp[n2] += dp[p] %mod
            # print(dp)
        return sum(dp[low:]) %mod
```

