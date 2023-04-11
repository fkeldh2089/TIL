# Removing Start from a String

```python
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        cnt = 0
        answer = ''
        for p in range(len(s)-1, -1, -1):
            if s[p] == "*":
                cnt += 1
            else:
                if cnt == 0:
                    ans.append(s[p])
                else:
                    cnt -= 1
        for p in range(len(ans)-1, -1, -1):
            answer += ans[p]
        return answer
            
```

