# Check Completeness of a Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        mf = 0
        while q:
            cur = q.pop()
            if mf == 0:
                if cur.left and cur.right:
                    q.appendleft(cur.left)
                    q.appendleft(cur.right)
                elif cur.left:
                    q.appendleft(cur.left)
                    mf = 1
                elif cur.right:
                    return False
                else:
                    mf = 1
            else:
                if cur.left or cur.right:
                    return False
        return True
```

