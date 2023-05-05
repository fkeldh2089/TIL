# Maximum Number of Vowels in a Substring of Given Length

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        if k ==1:
            for p in s:
                if p in vowels:
                    return 1
            else:
                return 0
        cnt = 0
        for p in range(k):
            if s[p] in vowels:
                cnt += 1
        i = 0
        mx = cnt
        j = k-1
        while j+1<len(s):
            j+=1
            if s[i] in vowels:
                cnt -= 1
            i+=1
            if s[j] in vowels:
                cnt += 1
            if cnt == k:
                return k
            if cnt > mx:
                mx = cnt
        return mx
```

