# Generate Parentheses

```python
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        recList = []
        def rec(n, st, cnt, cur):
            if cnt == n and cur ==0:
                recList.append(st)
            else:
                if cnt < n:
                    st1 = st+"("
                    rec(n, st1, cnt+1, cur+1)
                if cur>0:
                    st1 = st + ")"
                    rec(n, st1, cnt, cur-1)
        q = deque()
        q. append("()")
        rec(n, "", 0, 0)
        return recList
```

