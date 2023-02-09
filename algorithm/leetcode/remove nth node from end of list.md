# remove nth node from end of list

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tmp = head
        cnt = 1
        while True:
            if tmp.next:
                tmp = tmp.next
                cnt += 1
            else:
                break
        deltarget = head
        intarget = None
        for p in range(cnt-n):
            intarget = deltarget
            deltarget = deltarget.next

        inserttarget = deltarget.next
        if intarget:
            intarget.next = inserttarget
        else:
            head = head.next
        return head
            
```

