# Minimize Maximum of Array

```python
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        tot = 0
        for p in range(len(nums)):
            tot += nums[p]
            tmp = tot//(p+1) +  (1 if int(tot%(p+1)) else 0)
            if ans < tmp:
                ans = tmp

        
        return ans
```

