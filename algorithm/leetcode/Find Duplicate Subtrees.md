# Find Duplicate Subtrees

```python
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def inorder(node, m, ans):
            if (not node):
                return ""
            Str = "("
            Str += inorder(node.left, m, ans)
            Str += str(node.val)
            Str += inorder(node.right, m, ans)
            Str += ")"
            if Str in m:
                m[Str] += 1
                if m[Str]==2:
                    ans.append(node)
            else:
                m.update({Str:1})
            return Str
        m = dict()
        ans = []
        q = deque()
        q.append(root)
        inorder(root, m, ans)
        # print(m)
        # print(ans)
        # while q:
        #     R = q.pop()
        #     inorder(R, m)
        #     if R.left:
        #         q.appendleft(R.left)
        #     if R.right:
        #         q.appendleft(R.right)
        # print(m)
        return ans
```

