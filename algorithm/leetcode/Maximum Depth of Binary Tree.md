# Maximum Depth of Binary Tree

````python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        qu = deque()
        qu.append([root, 0])
        ret = 0
        if root:
            while qu:
                tmp, cnt = qu.popleft()
                if tmp.left or tmp.right:
                    if tmp.left:
                        qu.append([tmp.left, cnt + 1])
                    if tmp.right:
                        qu.append([tmp.right, cnt +1])
                else:
                    if cnt > ret:
                        ret = cnt
            return ret+1
        else:
            return 0
````

