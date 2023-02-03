# 3 Sum

```python
from itertools import combinations


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_dic = {}
        ans_list = []
        for p in range(len(nums)):
            if nums_dic.get(nums[p]):
                nums_dic[nums[p]] += 1
            else:
                nums_dic.update({nums[p]:1})
        for p1 in range(len(nums)):
            if p1>0 and nums[p1] == nums[p1-1]:
                continue
            nums_dic[nums[p1]] -= 1
            for p2 in range(p1+1, len(nums)):
                if p2>p1+1 and nums[p2] == nums[p2-1]:
                    continue
                nums_dic[nums[p2]] -= 1
                if -(nums[p1]+nums[p2])>=nums[p2] and nums_dic.get(-(nums[p1]+nums[p2])):
                    ans_list.append([nums[p1], nums[p2], -(nums[p1]+nums[p2])])
                nums_dic[nums[p2]] += 1
            nums_dic[nums[p1]] += 1
        return ans_list
        
        
```

