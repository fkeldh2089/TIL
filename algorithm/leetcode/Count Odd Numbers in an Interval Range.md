# Count Odd Numbers in an Interval Range

```python
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = low//2
        h = high//2
        if high%2:
            h += 1
        return h-l
```

