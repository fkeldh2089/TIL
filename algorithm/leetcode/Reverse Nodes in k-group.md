# Reverse Nodes in k-group

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        manu = head
        vals = []
        af = []
        while manu:
            vals.append(manu.val)
            manu=manu.next
        l = len(vals)
        cnt = 0
        for p in range(l):
            if p%k==0:
                cnt += 1
            if k*cnt-1-p%k<l:
                af.append(vals[k*cnt-1-p%k])
            else:
                cnt = 10000
                af.append(vals[p])
        manu = head
        idx = 0
        while manu:
            manu.val = af[idx]
            idx += 1
            manu = manu.next
        return head
```

