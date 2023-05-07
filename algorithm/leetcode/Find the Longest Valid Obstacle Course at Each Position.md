# Find the Longest Valid Obstacle Course at Each Position

```python
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        def findmid(li, n):
            l, i = 0, len(li)-1
            while l<i:
                mid = (l+i)//2
                if li[mid] >n:
                    i = mid-1
                elif li[mid] <n:
                    l = mid+1
                else:
                    l = mid
                    break
            if li[l] == n:
                while l+1 < len(li) and li[l+1] == n:
                    l += 1
                return l
            else:
                if li[l] > n:
                    return l-1
                else:
                    return l

                
        for p in range(len(obstacles)):
            obs = obstacles[p]
            if not lis or obs >= lis[-1]:
                lis.append(obs)
                obstacles[p] = len(lis)
            else:
                idx = findmid(lis, obs)
                # print(p, idx)
                lis[idx+1] = obs
                obstacles[p] = idx + 2
            # print("lis: ",lis)
            # print("ans: ",obstacles[:p+1])
        return obstacles
```

