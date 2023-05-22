# Top k Frequent Elements

```python
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        ans = []
        for num in nums:
            dic[num] += 1

        li = []
        for p in dic.items():
            li.append(p)

        li.sort(key=lambda x: -x[1])
        for p in range(k):
            ans.append(li[p][0])
        return ans
```

