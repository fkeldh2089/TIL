# Scramble String

```python
from collections import Counter


class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1: str, s2: str) -> bool:
        if(s1, s2) in self.memo:
            return self.memo[(s1, s2)]
        n = len(s1)
        if s1 == s2:
            self.memo[(s1, s2)]=True
            return True
        if len(s2) != n:
            self.memo[(s1, s2)]=False
            return False
        if Counter(s1) != Counter(s2):
            self.memo[(s1, s2)]=False
            return False

        for p in range(1, len(s1)):
            if self.isScramble(s1[:p], s2[:p]) and self.isScramble(s1[p:], s2[p:]):
                return True
            if self.isScramble(s1[:p], s2[n-p:]) and self.isScramble(s1[p:], s2[:n-p]):
                return True
        
        self.memo[(s1, s2)]=False
        return False
        # idx = 0
        # ANS = [False]
        # def isS(s1, s2):
        #     n = len(s1)
        #     n1 = len(s2)
        #     if s1 == s2:
        #         return True
        #     if n != n1:
        #         return False
        #     if Counter(s1) != Counter(s2):
        #         return False
        #     for p in range(1, len(s1)):
        #         if isS(s1[:p], s2[:p]) and isS(s1[p:], s2[p:]):
        #             return True
        #         if isS(s1[:p], s2[n-p:]) and isS(s1[p:], s2[:n-p]):
        #             return True
        #     return False
        # return isS(s1, s2)
        # dic1 = [0]*27
        # dic2 = [0]*27
        # dic3 = [0]*27
        # def rec(s1, s2):
        #     print(s1, s2)
        #     if s1 and s2:
        #         pass
        #     else:
        #         return 0
        #     if s1 == s2:
        #         print("same")
        #         return 0
        #     n = len(s1)
        #     if n <= 1:
        #         print("than")
        #         ANS[0] = False
        #         return
        #     for p in range(27):
        #         dic2[p] = 0
        #         dic3[p] = 0
        #     for p in range(n):
        #         dic2[ord(s1[p])-97] += 1
        #         dic3[ord(s1[p])-97] += 1
        #         dic2[ord(s2[-1-p])-97] -= 1
        #         dic3[ord(s2[p])-97] -= 1
        #         # print(dic2, not(dic2))
        #         # print(dic3, not(dic3))
        #         if p != n-1 and dic2 == dic1:
        #             print("hi1")
        #             print("1", s1[:p+1], s2[-1-p:])
        #             print("2", s1[p+1:], s2[:n-p-1])
        #             rec(s1[:p+1], s2[-1-p:])
        #             rec(s1[p+1:], s2[:n-p-1])
        #             break
        #         elif p!= n-1 and dic3 == dic1:
        #             print("hi")
        #             print("1", s1[:p+1], s2[:p+1] )
        #             print("2", s1[p+1:], s2[p+1:])
        #             rec(s1[:p+1], s2[:p+1])
        #             rec(s1[p+1:], s2[p+1:])
        #             break
        #     else:
        #         ANS[0] = False
        #         return 0


        # rec(s1, s2)
        # return ANS[0]
```

