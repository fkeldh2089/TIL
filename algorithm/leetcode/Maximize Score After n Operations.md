# Maximize Score After n Operations

```python
from math import gcd
from collections import defaultdict

class Solution:
    # def maxScore(self, nums: List[int]) -> int:
    #     visited = [0]*len(nums)
    #     answer = [0]
    #     dic = defaultdict()
    #     def DFS(n, step):
    #         # print(n, step)
    #         # print(visited)
    #         if step*2==len(nums):
    #             if answer[0] < n:
    #                 answer[0] = n
    #         else:
    #             for p1 in range(len(nums)):
    #                 if visited[p1]:
    #                     continue
    #                 visited[p1] =1
    #                 for p2 in range(len(nums)):
    #                     if visited[p2]:
    #                         continue
    #                     else:
    #                         if dic.get(str(nums[p1])+" "+str(nums[p2])):
    #                             tmp = dic[str(nums[p1])+" "+str(nums[p2])]
    #                         else:
    #                             tmp = gcd(nums[p1], nums[p2])
    #                             dic.update({str(nums[p1])+" "+str(nums[p2]):tmp})
    #                         visited[p2] = 1
    #                         DFS(n+tmp*(step+1), step+1)
    #                         visited[p2] = 0
    #                 visited[p1] = 0
    #     DFS(0, 0)
    #     return answer[0]
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def find(nums, k):
            ans, M = 0, len(nums)
            for i in range(M):
                for j in range(i+1, M):
                    t = nums[:i] + nums[i+1:j] + nums[j+1:]
                    ans = max(ans, k*gcd(nums[i], nums[j]) + find(t, k+1))
            return ans
          
        return find(tuple(nums), 1)
```

