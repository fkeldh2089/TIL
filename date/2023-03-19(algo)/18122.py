# 18122 색깔 하노이
import sys

sys.stdin = open("input_18122.txt")
# sys.setrecursionlimit(1000001)


# def getHanoi(n):
#     # print(n)
#     if n == 1:
#         return 3
    
#     else:
#         tmp = 4*(2**(n-1)-1)+4
#         # print(tmp)
#         return getHanoi(n-1)+tmp


N = int(input())
# for p in range(1, 10):
#     print(getHanoi(p))
ans = 3+8*(2**(N-1)-1)
print(ans%(10**9+7))

