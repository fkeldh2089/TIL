# Jump Game IV

```python
from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nums_dic= {}
        for p in range(len(arr)):
            if nums_dic.get(arr[p]):
                nums_dic[arr[p]].append(p)
            else:
                nums_dic.update({arr[p]:[p]})
        q = deque()
        q.append([0, 0])
        visited = [1] * (len(arr)+1)
        visited[-1] = 0
        while q:
            cur, cnt = q.pop()
            n = arr[cur]
            if cur == len(arr)-1:
                return cnt
            if nums_dic.get(n):
                for p in nums_dic[n]:
                    if p == cur:
                        if visited[cur+1]:
                            visited[cur+1] = 0
                            # if cur+1 == len(arr)-1:
                            #     return cnt +1
                            q.appendleft([cur+1, cnt + 1])
                        if visited[cur-1]:
                            visited[cur-1] = 0
                            q.appendleft([cur-1, cnt + 1])
                    else:
                        if visited[p]:
                            visited[p] = 0
                            # if p == len(arr)-1:
                            #     return cnt + 1
                            q.appendleft([p, cnt+1])
                nums_dic.pop(n)
            else:
                if visited[cur+1]:
                    visited[cur+1] = 0
                    # if cur+1 == len(arr)-1:
                    #     return cnt +1
                    q.appendleft([cur+1, cnt + 1])
                if visited[cur-1]:
                    visited[cur-1] = 0
                    q.appendleft([cur-1, cnt + 1])
        return 0
            



```

