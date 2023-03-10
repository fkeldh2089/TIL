# Linked List Random Node

```python
import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        # print(self, head)
        self.vals = []
        k = head
        while k != None:
            self.vals.append(k.val)
            k = k.next
        

    def getRandom(self) -> int:
        # print(self.vals)
        # random.choice(sel.vals)
        return random.choice(self.vals)
        

# obj = Solution(head)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

