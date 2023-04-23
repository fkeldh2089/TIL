# Restore the Array

```python
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        cnt = 0
        dp = [0]*(len(s)+1)
        dp[-1] = 1
        
        for p in range(len(s)-1, -1, -1):
            num = int(s[p])
            if num:
                idx = p+1
                while num<=k and idx<len(s)+1:
                    dp[p] += dp[idx]
                    if idx<len(s):
                        num = 10*num + int(s[idx])
                    idx += 1
                dp[p] %= (10**9 + 7)
            else:
                continue
        # print(dp)
        return dp[0]
```

