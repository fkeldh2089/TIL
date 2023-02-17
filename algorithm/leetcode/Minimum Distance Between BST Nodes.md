# Minimum Distance Between BST Nodes

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        mn = 10000000
        vals = []
        def rec(a):
            vals.append(a.val)
            if a.left:
                rec(a.left)
            if a.right:
                rec(a.right)
            return 0
        rec(root)
        vals.sort()
        ret = 1000000
        for p in range(len(vals)-1):
            tmp = abs(vals[p] - vals[p+1])
            if tmp < ret:
                ret = tmp
        return ret
```

