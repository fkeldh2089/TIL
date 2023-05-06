# Number of Subsequences That Satisfy the Given Sum Condition

```python
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, l = 0, len(nums)-1
        nums.sort()
        ans = 0
        mod = 10**9+7
        while i<= l:
            num1, num2 = nums[i], nums[l]
            if num1+num2 <= target:
                ans += 2**(l-i)
                i += 1
                # while i<=l and nums[i] == nums[i+1]:
                #     i += 1
            else:
                l -= 1
                # while i<=l and nums[l] == nums[l-1]:
                #     l -= 1
        
        return ans%mod
```

