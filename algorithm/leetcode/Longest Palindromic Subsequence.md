# Longest Palindromic Subsequence

```python
import sys

sys.setrecursionlimit(100000)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ans = 0
        @cache
        def findP(s, idx1, idx2):
            # print(s, idx1, idx2)
            if idx1 >idx2:
                return 0
            elif idx1 == idx2:
                return 1
            else:
                for p in range(idx2, idx1, -1):
                    if s[p] == s[idx1]:
                        return max(findP(s, idx1+1, idx2), findP(s, idx1+1, p-1)+2)
                else:
                    return max(findP(s, idx1+1, idx2), 1)
            
        # for p in range(len(s)):
            # print(findP(s, p, len(s)-1))
        ans = max(ans, findP(s, 0, len(s)-1))
        return ans
```

