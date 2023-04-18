# Merge String Alternately

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx = 0
        ans = ''
        while idx< len(word1) and idx < len(word2):
            ans += word1[idx]
            ans += word2[idx]
            idx += 1
        
        if idx<len(word1):
            ans += word1[idx:]
        elif idx<len(word2):
            ans += word2[idx:]
        
        return ans
```

