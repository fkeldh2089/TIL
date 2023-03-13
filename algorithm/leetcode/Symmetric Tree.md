# Symmetric Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        def find1(t):
            if t:
                ans1.append(t.val)
                find1(t.left)
                find1(t.right)
            else:
                ans1.append(101)
        def find2(t):
            if t:
                ans2.append(t.val)
                find2(t.right)
                find2(t.left)
            else:
                ans2.append(101)
        find1(root.left)
        find2(root.right)
        return ans1==ans2
```

