# Solving Questions with Brainpower

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0]*(len(questions)+1)
        for p in range(len(dp)-1):
            pnt, bp = questions[p]
            tar = p+bp+1
            if tar > len(questions):
                tar = len(questions)
            if dp[p] < dp[p-1]:
                dp[p] = dp[p-1]
            if dp[tar] < dp[p]+pnt:
                dp[tar] = dp[p]+pnt
        return dp[-1]
```

