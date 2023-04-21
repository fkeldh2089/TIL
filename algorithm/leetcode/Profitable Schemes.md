# Profitable Schemes

```python
from collections import deque
from pprint import pprint

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        answer = 0
        dp = [[0]*(n+1) for _ in range(minProfit+1)]
        dp[0][0] = 1
        for p in range(len(group)):
            g, p = group[p], profit[p]
            for q1 in range(minProfit, -1, -1):
                for q2 in range(n-g, -1, -1):
                    dp[min(minProfit, q1+p)][q2+g] += dp[q1][q2]
        return sum(dp[minProfit])%(10**9+7)

```

