# Minimum Time to Complete Trips

```python
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        i = 0
        l = 10**14
        while i<l:
            mid = (i+l)//2
            cnt = 0
            f=0
            for p in time:
                cnt += mid//p
                if cnt > totalTrips:
                    l = mid-1
                    f = 1
            if f==0:
                if cnt==totalTrips:
                    break
                else:
                    i = mid+1
        mid = (i+l)//2+1
        cnt = totalTrips
        while cnt>=totalTrips:
            mid -= 1
            cnt = 0
            for p in time:
                cnt += mid//p
        return mid+1
```

