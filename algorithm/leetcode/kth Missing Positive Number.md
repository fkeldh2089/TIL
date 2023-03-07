# kth Missing Positive Number

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 1
        cnt2 = 0
        for p in arr:
            if cnt == p:
                cnt += 1
            else:
                cnt2 += p-cnt
                cnt = p+1
            if cnt2 >= k:
                return cnt-2+ (k-cnt2)
        return cnt-1 + (k-cnt2)
```

