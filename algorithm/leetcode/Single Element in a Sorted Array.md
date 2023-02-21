# Single Element in a Sorted Array

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        l = 0
        r = len(nums)-1
        while l< r:
            mid = (l + r)//2
            if mid %2:
                if nums[mid]==nums[mid+1]:
                    r= mid-1
                elif nums[mid]==nums[mid-1]:
                    l = mid+1
                else:
                    return nums[mid]
            else:
                if nums[mid]==nums[mid+1]:
                    l= mid+1
                elif nums[mid]==nums[mid-1]:
                    r = mid-1
                else:
                    return nums[mid]
        return nums[l]
```



