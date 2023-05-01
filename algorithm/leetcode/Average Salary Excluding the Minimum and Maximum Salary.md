# Average Salary Excluding the Minimum and Maximum Salary

```python
class Solution:
    def average(self, salary: List[int]) -> float:
        mn = 10**6+1
        mx = 0
        tot = 0
        for s in salary:
            if s>mx:
                mx = s
            if s<mn:
                mn = s
            tot += s
        return round(((tot-mn-mx)/(len(salary)-2)), 5)
```

