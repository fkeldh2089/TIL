# Boats to Save People

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i, l = 0, len(people)-1
        ans = 0
        # print(people)
        while i<=l:
            cur1 = people[l]
            if cur1 + people[i] <=limit:
                i += 1
                l -= 1
                ans += 1
            else:
                l -= 1
                ans += 1
            # print(i, l)
        return ans
```

