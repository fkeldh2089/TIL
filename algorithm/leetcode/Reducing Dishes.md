# Reducing Dishes

```python
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        # print(satisfaction)
        ans = 0
        tmp = 0
        for p in range(len(satisfaction)):
            tmp += satisfaction[p]
            if tmp > 0:
                ans += tmp
            else:
                break
        return ans
```

