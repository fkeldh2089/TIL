# Minimum Cost for tickets

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [10000000]*(367)
        dp[0] = 0
        idx = 0
        for p in range(len(dp)-1):
            if idx<len(days):
                if p == days[idx]:
                    if dp[p+1] > dp[p]+costs[0]:
                        dp[p+1] = dp[p]+costs[0]
                    idx += 1
                else:
                    if dp[p+1] > dp[p]:
                        dp[p+1] = dp[p]
                if p+7 <367 and dp[p+7] > dp[p]+costs[1]:
                    dp[p+7] = dp[p] + costs[1]
                elif p+7>=367 and dp[-1] > dp[p]+costs[1]:
                    dp[-1] = dp[p] + costs[1]
                if p+30 <367 and dp[p+30] > dp[p]+costs[2]:
                    dp[p+30] = dp[p] + costs[2]
                elif p+30 >=367 and dp[-1] > dp[p]+costs[2]:
                    dp[-1] = dp[p] + costs[2]
            else:
                if dp[p+1] > dp[p]:
                    dp[p+1] = dp[p]
        # print(dp)
        # if dp[-1] > costs[2]:
        #     dp [-1] = costs[2]
        # for p in range(len(dp)-7):
        #     if dp[p+7] > dp[p]+costs[1]:
        #         dp[p+7] = dp[p] + costs[1]
        # print(dp)
        return dp[-1]
```

