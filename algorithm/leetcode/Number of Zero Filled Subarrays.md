# Number of Zero Filled Subarrays

```python
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for p in range(len(nums)):
            if nums[p] == 0:
                cnt += 1
            else:
                if cnt>0:
                    ans += (cnt*(cnt+1))//2
                    cnt = 0
        ans += (cnt*(cnt+1))//2
        return ans
```

