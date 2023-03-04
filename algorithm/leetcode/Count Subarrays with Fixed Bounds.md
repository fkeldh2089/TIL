# Count Subarrays with Fixed Bounds

```python
from collections import deque


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        boundary = -1
        prevMinKIndex = -1
        prevMaxKIndex = -1

        for i, num in enumerate(nums):
            # 해당 범위를 넘는 값을 경계로 잡음
            if num < minK or num > maxK:
                boundary = i
            if num == minK:
                prevMinKIndex = i
            if num == maxK:
                prevMaxKIndex = i
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - boundary)

        return ans
```

