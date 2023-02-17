# Find the Index of the First Occurrence in a String

```python
import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pat = re.compile(needle)
        a = pat.search(haystack)
        if a:
            return a.span()[0]
        return -1
```

