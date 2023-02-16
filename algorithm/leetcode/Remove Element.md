# Remove Element

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        idx = 0
        l = len(nums)
        while idx + cnt < l:
            if nums[idx] == val:
                nums.pop(idx)
                cnt += 1
            else:
                idx += 1

        return l-cnt
```

