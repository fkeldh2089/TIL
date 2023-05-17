# Maximum Twin Sum of a Linked List

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cur = head
        li = []
        mx = 0
        while cur:
            li.append(cur.val)
            cur = cur.next
        for p in range(len(li)//2):
            tmp = li[p]+li[-1-p]
            if tmp > mx:
                mx = tmp
        return mx
```

