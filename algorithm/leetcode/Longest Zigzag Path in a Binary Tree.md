# Longest Zigzag Path in a Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        @cache
        def findZig(r, d, cnt):  # 루트, d는 그전 방향 0, 1
            nonlocal ans
            if r == None:
                if ans < cnt:
                    ans = cnt
                
            elif d:
                findZig(r.left, 0, cnt+1)
                findZig(r.right, 1, 0)
                # findZig(r.right, 0, 0)
            else:
                findZig(r.left, 0, 0)
                # findZig(r.left, 1, 0)
                findZig(r.right, 1, cnt+1)
            
        findZig(root.right, 1, 0)
        findZig(root.left, 0, 0)
        return ans
```

