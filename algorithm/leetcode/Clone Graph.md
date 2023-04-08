# Clone Graph

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque, defaultdict


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if node:
            k = Node(node.val)
            q= deque()
            q.append(node)
            nodes = defaultdict(int)
            nodes[node.val] = k
            while q:
                cur = q.pop()
                nd = nodes[cur.val]
                for p in cur.neighbors:
                    if nodes[p.val]:
                        pass
                    else:
                        nodes[p.val] = Node(p.val)
                        q.appendleft(p)
                    nd.neighbors.append(nodes[p.val])
        else:
            return node
        return k
```

