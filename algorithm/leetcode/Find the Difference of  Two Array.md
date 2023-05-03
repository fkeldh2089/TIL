# Find the Difference of  Two Array

```python
from collections import defaultdict


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dic = defaultdict(int)
        answer = [[], []]
        for num in nums1:
            dic[num] += 1
        for num in nums2:
            dic[num] -= 10000
        
        for idx, item in dic.items():
            if item>0:
                answer[0].append(idx)
            else:
                if item%10000 == 0:
                    answer[1].append(idx)
        
        return answer
```

