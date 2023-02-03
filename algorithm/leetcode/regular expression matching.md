# regular expression matching

```python
class Solution(object):
    def isMatch(self, s, p):
        pattern = re.compile(p)
        matched = pattern.match(s)
        if matched and matched.span()[1]-matched.span()[0]==len(s):
            return True
        else:
            return False
        
```

