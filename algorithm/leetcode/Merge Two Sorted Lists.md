# Merge Two Sorted Lists

```python
from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = deque()
        while list1 != None:
            l1.append(list1.val)
            list1 = list1.next

        l2 = deque()
        while list2 != None:
            l2.append(list2.val)
            list2 = list2.next
        
        b = None
        while l1 and l2:
            if l1[-1] > l2[-1]:
                tmp = l1.pop()
            else:
                tmp = l2.pop()
            b = ListNode(tmp, b)
        
        while l1:
            tmp = l1.pop()
            b = ListNode(tmp, b)
        
        while l2:
            tmp = l2.pop()
            b = ListNode(tmp, b)
        
        return b
```

