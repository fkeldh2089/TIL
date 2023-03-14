# Sum Root to Leaf Number

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        Ans = [0]
        def getNums(t, s):
            if not t.left and not t.right:
                s += str(t.val)
                if s:
                    Ans[0] += int(s)
            else:
                if t.left:
                    getNums(t.left, s+str(t.val))
                if t.right:
                    getNums(t.right, s+str(t.val))
        if root:
            getNums(root, '')
        else:
            return 0
        return Ans[0]
```

