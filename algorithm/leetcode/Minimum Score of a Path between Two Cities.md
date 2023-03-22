# Minimum Score of a Path between Two Cities

```python
from collections import defaultdict, deque


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        gra = defaultdict(list)
        dis = defaultdict(int)
        visited = []
        for p in range(len(roads)):
            gra[roads[p][0]].append(roads[p][1])
            gra[roads[p][1]].append(roads[p][0])
            if dis[roads[p][0]]:
                if dis[roads[p][0]] > roads[p][2]:
                    dis[roads[p][0]] = roads[p][2]
            else:
                dis[roads[p][0]] = roads[p][2]
            if dis[roads[p][1]]:
                if dis[roads[p][1]] > roads[p][2]:
                    dis[roads[p][1]] = roads[p][2]
            else:
                dis[roads[p][1]] = roads[p][2]
        
        q = deque()
        q.append(1)
        ans = 10000000
        # print(gra)
        # print(dis)
        while q:
            cur = q.pop()
            for p in gra[cur]:
                q.appendleft(p)
                if ans > dis[p]:
                    ans = dis[p]
            gra.pop(cur)
        return ans
```

