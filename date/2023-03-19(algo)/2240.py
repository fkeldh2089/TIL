# 2240 자두나무
import sys
from pprint import pprint
sys.stdin = open("input_2240.txt")


T, W = map(int, input().split())
dp = [[0]*(T+1) for _ in range(W+2)]

for p1 in range(T):
    n = int(input())
    if p1<W+1:
        for p2 in range(p1+1):
            if n %2 == (p2+1)%2:
                if dp[p2][p1+1] == 0:
                    dp[p2][p1+1] = dp[p2][p1] +1
                if dp[p2][p1]>dp[p2+1][p1]+1:
                    dp[p2+1][p1+1] = dp[p2][p1]
            else:
                if dp[p2][p1+1] == 0:
                    dp[p2][p1+1] = dp[p2][p1]
                if dp[p2][p1]+1>dp[p2+1][p1]:
                    dp[p2+1][p1+1] = dp[p2][p1]+1
    else:
        for p2 in range(W+1):
            if n%2 == (p2+1)%2:
                if dp[p2][p1+1] == 0:
                    dp[p2][p1+1] = dp[p2][p1] +1
                if dp[p2][p1]>dp[p2+1][p1]+1:
                    dp[p2+1][p1+1] = dp[p2][p1]
            else:
                if dp[p2][p1+1] == 0:
                    dp[p2][p1+1] = dp[p2][p1]
                if dp[p2][p1]+1>dp[p2+1][p1]:
                    dp[p2+1][p1+1] = dp[p2][p1]+1

mx = 0
for p in range(len(dp)-1):
    if mx < dp[p][-1]:
        mx = dp[p][-1]
print(mx)