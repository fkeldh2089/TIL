# Dota2 Senate

```python
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        nums = deque()
        idx = 0
        while idx<len(senate):
            if senate[idx] == "R":
                f = 1
            else:
                f = -1
            for p in range(idx, len(senate)):
                if senate[idx] == senate[p]:
                    pass
                else:
                    nums.append(f*(p-idx))
                    idx = p
                    break
            else:
                nums.append(f*(p+1-idx))
                idx = p+1
        # print(nums)
        cnt = 0
        f = 1
        while f:
            f = 0
            for p in range(len(nums)):
                # print(cnt)
                if cnt * nums[p] >=0:
                    cnt += nums[p]
                else:
                    f = 1
                    if abs(nums[p]) > abs(cnt):
                        cnt += nums[p]
                        nums[p] = cnt
                    else:
                        cnt += nums[p]
                        nums[p] = 0
        # print(nums)
        if cnt < 0:
            return "Dire"
        else:
            return "Radiant"
```

