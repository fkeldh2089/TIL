# Kids with the Greatest Number of Candies

```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        mx = max(candies)
        tar = mx-extraCandies
        for candy in candies:
            if candy < tar:
                ans.append(False)
            else:
                ans.append(True)
        return ans
```

