# Number of Ways to Form a Target String Given a Dictionary

```python
from collections import defaultdict


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = [[0]*(len(words[0])+1) for _ in range(len(target)+1)]
        aps = {}
        for p in range(len(words[0])):
            aps.update({p:{}})
            for word in words:
                if aps[p].get(word[p]):
                    aps[p][word[p]] += 1
                else:
                    aps[p].update({word[p]:1})
        # print(aps)

        for p1 in range(len(target)):
            for p2 in range(p1, len(words[0])-len(target)+p1+1):
                if aps[p2].get(target[p1]):
                    if p1 == 0:
                        dp[p1][p2] += aps[p2][target[p1]]+dp[p1][p2-1]
                    else:
                        dp[p1][p2] += aps[p2][target[p1]]*dp[p1-1][p2-1]+dp[p1][p2-1]
                else:
                    dp[p1][p2] = dp[p1][p2-1]
                # print(p1, p2, dp)
        
        # print(dp)


        return (dp[-2][-2])%(10**9+7)
```

