# Invert Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return root
        def rec(t):
            if t == None:
                return
            t.left, t.right = t.right,t.left
            rec(t.left)
            rec(t.right)
        rec(root)
        return root
```

