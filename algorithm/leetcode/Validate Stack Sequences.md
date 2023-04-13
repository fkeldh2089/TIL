# Validate Stack Sequences

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        qu = []
        idx1 = 0
        idx2 = 0
        f = 1
        while 1:
            if idx1 == len(pushed) and idx2 == len(popped):
                break
            if qu and idx2<len(popped):
                if qu[-1] == popped[idx2]:
                    qu.pop()
                    idx2 += 1
                elif idx1<len(pushed):
                    qu.append(pushed[idx1])
                    idx1 += 1
                else:
                    f = 0
                    break
            else:
                if idx1 < len(pushed):
                    qu.append(pushed[idx1])
                    idx1 += 1
                else:
                    f = 0
                    break
        if f:
            return True
        else:
            return False
```

