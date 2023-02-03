# median of two sorted arrays

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n:
            if n %2:
                return nums[n//2]
            else:
                return (nums[n//2]+nums[n//2 -1])/2

        else:
            return 0
```
