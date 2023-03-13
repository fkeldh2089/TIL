# Merge K Sorted Lists

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        idxs = [0] * len(lists)
        nodes = [0] * len(lists)
        for p in range(len(lists)):
            if lists[p]:
                idxs[p] = lists[p].val
                nodes[p] = lists[p]
            else:
                idxs[p] = 100000
        mn = min(idxs)
        if mn >10000:
            return None
        midx = idxs.index(mn)
        ans = ListNode(mn)
        if nodes[midx].next:
            nodes[midx] = nodes[midx].next
            idxs[midx] = nodes[midx].val
        else:
            idxs[midx] = 100000
        k = ans
        while 1:
            mn = min(idxs)
            if mn >10000:
                break
            midx = idxs.index(mn)
            tmp = ListNode(mn)
            if nodes[midx].next:
                nodes[midx] = nodes[midx].next
                idxs[midx] = nodes[midx].val
            else:
                idxs[midx] = 100000
            k.next = tmp
            k = tmp
        return ans
```

