# Sign of the Product of an Array

```python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        f = 1
        for num in nums:
            if num<0:
                f *= -1
            elif num == 0:
                return 0
        return f
```

