# longest palindromic substring

```python
from collections import deque


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        odd = deque()
        even = deque()
        mn = 0
        for p in range(len(s)):
            if p+1<len(s) and s[p] == s[p+1]:
                even.append(p)
            if p+2<len(s) and s[p] == s[p+2]:
                odd.append(p+1)
        while odd:
            idx = odd.pop()
            tmp = 2
            while idx+tmp<len(s) and idx-tmp>=0:
                if s[idx+tmp]==s[idx-tmp]:
                    tmp += 1
                else:
                    break
            if mn < 2*(tmp-1) + 1:
                ans = [idx, tmp-1, "odd"]
                mn = 2*(tmp-1) + 1
        while even:
            idx = even.pop()
            tmp = 1
            while idx+tmp+1<len(s) and idx-tmp>=0:
                if s[idx+tmp+1] == s[idx-tmp]:
                    tmp += 1
                else:
                    break
            if mn < 2+ 2*(tmp-1):
                ans = [idx, tmp-1, "even"]
                mn = 2+ 2*(tmp-1)
        if mn:
            ret = convertAnstoRet(s, ans)
            return ret
        else:
            return s[0]
    
def convertAnstoRet(s, ans):
    if ans[2] == "odd":
        return s[ans[0]-ans[1]:ans[0]+ans[1]+1]
    else:
        return s[ans[0]-ans[1]:ans[0]+ans[1]+2]
```



