# Add to Array Form of Integer

```python
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        orNum = int("".join(map(str, num)))
        ans = str(k + orNum)
        return list(map(int, ans))
```

