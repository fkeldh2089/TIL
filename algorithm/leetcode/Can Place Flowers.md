# Can Place Flowers

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for p in range(len(flowerbed)):
            if flowerbed[p] == 0:
                f1 = 1
                f2 = 1
                if p-1>=0 and flowerbed[p-1]:
                    f1 = 0
                if p+1<len(flowerbed) and flowerbed[p+1]:
                    f2 = 0
                if f1 and f2:
                    flowerbed[p] = 1
                    n -= 1
            if n <=0:
                return True
        return False
```

