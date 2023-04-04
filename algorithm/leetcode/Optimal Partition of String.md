# Optimal Partition of String

```python
from collections import defaultdict


class Solution:
    def partitionString(self, s: str) -> int:
        idx = 0
        ans = 0
        while idx<len(s)-1:
            dic = defaultdict(int)
            for p in range(idx, len(s)):
                if dic[s[p]] > 0:
                    ans += 1
                    # print(p)
                    break
                else:
                    dic[s[p]] += 1
                idx += 1

        return ans+1
```

