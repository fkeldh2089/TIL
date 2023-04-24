# Last Stone Weight

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = list(map(lambda x: -x, stones))
        heapq.heapify(hp)
        while len(hp)>1:
            tmp1 = heapq.heappop(hp)
            tmp2 = heapq.heappop(hp)
            tmp3 = -abs(tmp1-tmp2)
            if tmp3:
                heapq.heappush(hp, tmp3)
        if hp:
            return -hp[0]
        else:
            return 0
```

