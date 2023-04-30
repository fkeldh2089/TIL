# Remove Max Number of Edges to Keep Graph Fully Traversable

```python
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ufa, ufb = UnionFind(n), UnionFind(n)
        ans = 0
        for t, u, v in edges:
            if t == 3:
                if not ufa.union(u - 1, v - 1):
                    ans += 1
                else:
                    ufb.union(u - 1, v - 1)
        for t, u, v in edges:
            if t == 1:
                if not ufa.union(u - 1, v - 1):
                    ans += 1
            elif t == 2:
                if not ufb.union(u - 1, v - 1):
                    ans += 1
        if ufa.cnt != 1 or ufb.cnt != 1:
            return -1
        return ans

class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.cnt = n

    def union(self, x, y):
        p1, p2 = self.find(x), self.find(y)
        if p1 != p2:
            self.parents[p2] = p1
            self.cnt -= 1
            return True
        else:
            return False

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
```

