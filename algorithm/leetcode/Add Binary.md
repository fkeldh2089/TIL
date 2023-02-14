# Add Binary

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)<len(b):
            a,b = b,a
        a = list(a)
        b = list(b)
        answer = []
        c = 0
        ret = ''
        while a and b:
            a1 = int(a.pop())
            b1 = int(b.pop())
            tmp = a1+b1+c
            if tmp == 2:
                answer.append(0)
                c = 1
            elif tmp == 1:
                answer.append(1)
                c = 0
            elif tmp == 3:
                answer.append(1)
                c = 1
            else:
                answer.append(0)
                c = 0
        while a:
            a1 = int(a.pop())
            tmp = a1 + c
            if tmp == 2:
                answer.append(0)
                c = 1
            elif tmp == 1:
                answer.append(1)
                c = 0
            elif tmp == 3:
                answer.append(1)
                c = 1
            else:
                answer.append(0)
                c = 0
        if c:
            answer.append(1)

        for p in range(len(answer)-1, -1, -1):
            ret += str(answer[p])
        if ret:
            return ret
        else:
            return '0'
```

