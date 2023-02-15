# Swap Nodes in Pairs

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k = head
        while k and k.next:
            tmp1 = k.val
            tmp2 = k.next.val
            k.val = tmp2
            k.next.val = tmp1
            k = k.next.next
        return head
```

