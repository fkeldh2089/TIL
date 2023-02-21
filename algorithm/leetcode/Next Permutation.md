# Next Permutation

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mn = 1000
        idx = len(nums)-1
        while idx>0:
            if nums[idx] <= nums[idx-1]:
                idx -= 1
            else:
                break
        
        if idx == 0:
            nums.sort()
        
        else:
            for p in range(idx-1, len(nums)):
                if nums[p]>nums[idx-1]:
                    if nums[p]<mn:
                        mn = nums[p]
                        mnidx = p
            nums[idx-1], nums[mnidx] = nums[mnidx], nums[idx-1]
            nums[idx:]=sorted(nums[idx:])
        
        
        
```

