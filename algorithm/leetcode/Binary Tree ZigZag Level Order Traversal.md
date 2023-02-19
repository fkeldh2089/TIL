# Binary Tree ZigZag Level Order Traversal

```python
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        qu = deque()
        qu.append(root)
        f = 1
        ans = [[root.val]]
        while qu:
            row = []
            nextqu = deque()
            while qu:
                tmp = qu.pop()
                if f == 0:
                    if tmp.left:
                        row.append(tmp.left.val)
                        nextqu.append(tmp.left)
                    if tmp.right:
                        row.append(tmp.right.val)
                        nextqu.append(tmp.right)
                elif f == 1:
                    if tmp.right:
                        row.append(tmp.right.val)
                        nextqu.append(tmp.right)
                    if tmp.left:
                        row.append(tmp.left.val)
                        nextqu.append(tmp.left)
            if row:
                ans.append(row)
            qu = nextqu
            if f == 0:
                f = 1
            else:
                f = 0
        return ans
```

