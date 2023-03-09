# Linked List Cycle II

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import defaultdict


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = defaultdict()
        cur = head
        cnt = 0
        while head:
            for i, p in nodes.items():
                if cur == p:
                    return cur
            else:
                nodes[cnt] = cur
            if cur.next:
                cur = cur.next
                cnt += 1
            else:
                return None
        return None
```

