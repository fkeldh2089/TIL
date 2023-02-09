# 4 sum

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        numdic = {}
        answer = []
        for p in nums:
            if numdic.get(p):
                numdic[p] += 1
            else:
                numdic.update({p:1})
        
        for p1 in range(len(nums)-3):
            if p1>0 and nums[p1] == nums[p1-1]:
                continue
            numdic[nums[p1]] -= 1
            for p2 in range(p1+1, len(nums)-2):
                if p2>p1+1 and nums[p2] == nums[p2-1]:
                    continue
                numdic[nums[p2]] -= 1
                for p3 in range(p2+1, len(nums)-1):
                    if p3>p2+1 and nums[p3] == nums[p3-1]:
                        continue
                    numdic[nums[p3]] -= 1
                    tmp = target - nums[p1] - nums[p2] - nums[p3]
                    if tmp >= nums[p3] and numdic.get(tmp) and numdic[tmp]>0:
                        answer.append([nums[p1], nums[p2], nums[p3], tmp])
                    numdic[nums[p3]] += 1
                numdic[nums[p2]] += 1
            numdic[nums[p1]] += 1
        return answer
                    
            




        
```

