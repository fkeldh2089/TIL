# Smallest Number in Infinite Set

```python
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.cnt = 1
        self.numSet = set()
        self.nums = []
        

    def popSmallest(self) -> int:
        if self.nums:
            ret = heapq.heappop(self.nums)
            self.numSet.discard(ret)
            return ret
        else:
            self.cnt += 1
            return self.cnt -1
        

    def addBack(self, num: int) -> None:
        if num < self.cnt:
            if num in self.numSet:
                pass
            else:
                self.numSet.add(num)
                heapq.heappush(self.nums, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
```

