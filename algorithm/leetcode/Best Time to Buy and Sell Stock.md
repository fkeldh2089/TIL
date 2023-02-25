# Best Time to Buy and Sell Stock

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 100000
        mx = 0
        for p in range(len(prices)):
            if prices[p] < mn:
                mn = prices[p]
            if mx < prices[p] - mn:
                mx = prices[p] - mn
        return mx
```

