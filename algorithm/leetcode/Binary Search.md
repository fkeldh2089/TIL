# Binary Search

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, l = 0, len(nums)-1
        while i<=l:
            print(i, l)
            mid = (i+l)//2
            if nums[mid]<target:
                i = mid+1
            elif nums[mid]>target:
                l = mid-1
            else:
                return mid
        return -1
```

