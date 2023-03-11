# Convert Sorted List to Binary Search Tree

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        curr, count = head, 0
        while curr:
            curr = curr.next
            count += 1
        def treeify(i: int, j: int) -> TreeNode:
            if j < i: return None
            mid, node = i + j >> 1, TreeNode()
            node.left = treeify(i, mid - 1)
            node.val, curr[0] = curr[0].val, curr[0].next
            node.right = treeify(mid + 1, j)
            return node
        curr = [head]
        return treeify(1, count)
```

