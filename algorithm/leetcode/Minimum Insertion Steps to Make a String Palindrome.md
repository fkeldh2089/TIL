# Minimum Insertion Steps to Make a String Palindrome

```python
from collections import deque
from pprint import pprint


class Solution:
    def minInsertions(self, s: str) -> int:
        answer = 500
        dp = [[500]*(len(s)+1) for _ in range(len(s)+1)]
        dp[0][0] = 0
        for p1 in range(len(s)):
            for p2 in range(len(s)):
                if p1 >= len(s)-1-p2:
                    if answer > dp[p1][p2]:
                        answer = dp[p1][p2]
                    break
                if s[p1] == s[len(s)-1-p2]:
                    if dp[p1][p2] < dp[p1+1][p2+1]:
                        dp[p1+1][p2+1] = dp[p1][p2]
                if dp[p1][p2]+1 < dp[p1][p2+1]:
                    dp[p1][p2+1] = dp[p1][p2]+1
                if dp[p1][p2]+1 < dp[p1+1][p2]:
                    dp[p1+1][p2] = dp[p1][p2]+1
        for p1 in range(len(s)):
            p2 = len(s)-p1
            if answer > dp[p1][p2]:
                answer = dp[p1][p2]
        # pprint(dp)
        # q = deque()
        # q.append([0, 0])
        # while q:
        #     curS, curE = q.pop()
        #     curE2 = len(s)-1-curE
        #     if curS>=curE2:
        #         # print(curS,curE, curE2)
        #         if answer > dp[curS][curE]:
        #             answer = dp[curS][curE]
        #         continue
        #     S, E = s[curS], s[curE2]
        #     if S == E:
        #         if dp[curS+1][curE+1] > dp[curS][curE]:
        #             dp[curS+1][curE+1] = dp[curS][curE]
        #             q.append([curS+1,curE+1])
        #     if dp[curS+1][curE] > dp[curS][curE]+1:
        #         dp[curS+1][curE] = dp[curS][curE]+1
        #         q.append([curS+1,curE])
        #     if dp[curS][curE+1] > dp[curS][curE]+1:
        #         dp[curS][curE+1] = dp[curS][curE]+1
        #         q.append([curS,curE+1])
            # pprint(dp)
        return answer
```

