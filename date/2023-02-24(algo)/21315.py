# 21315 카드섞기
import sys
sys.stdin = open("input_21315.txt")

N = int(input())
Cards = list(map(int, input().split()))

ans1 = 0
ans2 = 0

mx = 0
idx = 0
for p in range(N):
    if Cards[p]>mx:
        mx = Cards[p]
        idx = p

while idx >1:
    idx = idx//2
    ans2 += 1


p2 = N - Cards[0]
while p2>1:
    p2 = p2//2
    ans1 += 1

print(ans1, ans2)

    