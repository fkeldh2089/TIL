# Maximum Subsequence Score

```python
import heapq


class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        ans = 0
        for p in range(len(nums1)):
            nums.append([nums2[p], nums1[p]])
        
        nums.sort(key=lambda x: (x[0], x[1]))
        # print(nums)

        heap = []
        numSum = 0
        while nums:
            cur = nums.pop()
            if len(heap)<k:
                heapq.heappush(heap, cur[1])
                numSum += cur[1]
                if len(heap)==k:
                    ans = numSum*cur[0]
            else:
                if heap[0] < cur[1]:
                    numSum -= heapq.heappop(heap)
                    heapq.heappush(heap, cur[1])
                    numSum += cur[1]
                    if ans < numSum*cur[0]:
                        ans = numSum*cur[0]
        return ans
```

