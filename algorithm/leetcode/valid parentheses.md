# valid parentheses

```python
from collections import deque


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = deque()
        for p in s:
            if p == "(" or p=="{" or p == "[":
                q.append(p)
            elif q:
                val = q.pop()
                if p == ")" and val=="(":
                    pass
                elif p == "}" and val=="{":
                    pass
                elif p == "]" and val=="[":
                    pass
                else:
                    return False
            else:
                return False
        if q:
            return False
        else:
            return True
```

