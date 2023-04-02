# Successful Pairs of Speels and Potions

```python
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        @cache
        def midfind(n):
            l = 0
            r = len(potions)
            while l<r:
                mid = (l+r)//2
                if n*potions[mid] >= success:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        return [len(potions)-midfind(p) for p in spells]
```

