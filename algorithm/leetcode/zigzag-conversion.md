# zigzag-conversion

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        ans = ''
        num = len(s)
        for p in range(numRows):
            tmp = p
            while tmp < num:
                ans += s[tmp]
                if p != 0 and p != numRows-1:
                    tmp2 = (numRows-1 - p)*2
                    if tmp + tmp2 < num:
                        ans += s[tmp+tmp2]
                tmp += 2*numRows -2
        return ans
```

