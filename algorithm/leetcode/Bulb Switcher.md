# Bulb Switcher

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n == 0:
            return 0
        cnt = 1
        while cnt**2<=n:
            cnt += 1
        return cnt-1
```

