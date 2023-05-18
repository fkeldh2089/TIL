# Minimum Number of  Verticles to Reach All Nodes

```python
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = [0]*n
        for p in range(len(edges)):
            visited[edges[p][1]] += 1
        
        return [i for i, val in enumerate(visited) if val == 0]
```

