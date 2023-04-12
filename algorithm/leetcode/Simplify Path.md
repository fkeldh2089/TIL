# Simplify Path

```python
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        cnt =0
        q = deque()
        while paths:
            cur = paths.pop()
            if cur == ".":
                pass
            elif cur == "..":
                cnt += 1
            elif cur == "":
                pass
            else:
                if cnt == 0:
                    q.appendleft(cur)
                else:
                    cnt -= 1
        ans = ""
        for p in q:
            ans += "/"+p
        
        if ans:
            return ans
        else:
            return "/"
```

