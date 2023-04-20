# Maximum Width of Binary Tree

```python
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 1
        qu = deque()
        qu.append(root)
        while qu:
            q2 = deque()
            q2 = qu
            qu = deque()
            cnt = 0
            while q2:
                cur = q2.pop()
                if isinstance(cur, int):
                    qu.appendleft(2*cur)
                    cnt += 2*cur
                else:
                    if cur.right:
                        qu.appendleft(cur.right)
                    else:
                        qu.appendleft(1)
                    if cur.left:
                        qu.appendleft(cur.left)
                    else:
                        qu.appendleft(1)
                    cnt += 2
            # print(qu,cnt)
            while qu and isinstance(qu[-1], int):
                cnt -= qu.pop()
            while qu and isinstance(qu[0], int):
                cnt -= qu.popleft()
            
            if ans < cnt:
                ans = cnt
        
        return ans
```

