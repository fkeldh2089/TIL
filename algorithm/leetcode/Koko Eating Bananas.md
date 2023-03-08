# Koko Eating Bananas

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = 10**9
        while l < r:
            mid = (l+r)//2
            if mid == 0:
                return 1
            cnt = 0
            for p in piles:
                cnt += p//mid
                if p%mid:
                    cnt += 1
                if cnt > h:
                    l = mid+1
                    break
            else:
                if cnt == h:
                    r = mid
                else:
                    r = mid
        return l
```

