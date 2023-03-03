# String Compression

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        l = len(chars)
        idx = 0
        cnt = 0
        tmp = ""
        ans = 0
        while idx<len(chars):
            cnt1 = 1
            tmp = chars[idx]
            while idx+1<len(chars):
                if chars[idx+1]==tmp:
                    chars.pop(idx+1)
                    cnt1 += 1
                else:
                    break
            if cnt1>1:
                cnt1 = str(cnt1)
                for p in range(len(cnt1)):
                    chars.insert(idx+p+1, cnt1[p])
                idx = idx+p+2
            else:
                idx = idx + 1
            

        return len(chars)
```

