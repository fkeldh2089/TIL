# Remove Duplicates from Sorted Array

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx, cnt = 0, 0
        while idx<len(nums) and nums[idx] != "_":
            if idx>0:
                if nums[idx] == nums[idx-1]:
                    nums.pop(idx)
                    nums.append("_")
                else:
                    idx += 1
            else:
                idx += 1
            cnt += 1
        return idx
```

