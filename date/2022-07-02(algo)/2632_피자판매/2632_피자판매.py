# 2632 피자
import sys
from pprint import pprint
from collections import defaultdict
sys.stdin = open('input_2632.txt')

N = int(input())
A, B = map(int, input().split())
pizzaA = [int(input()) for _ in range(A)]
pizzaB = [int(input()) for _ in range(B)]
sumA = sum(pizzaA)
sumB = sum(pizzaB)
pizzaA += pizzaA[:-1]
pizzaB += pizzaB[:-1]

pizzaAcut = defaultdict(int)
pizzaBcut = defaultdict(int)
pizzaAcut[0] = 1
pizzaBcut[0] = 1
pizzaAcut[sumA] = 1
pizzaBcut[sumB] = 1
for p1 in range(0, A):
    for p2 in range(p1+1, p1+A):
        tmp = sum(pizzaA[p1: p2])
        if tmp > N:
            break
        else:
            pizzaAcut[tmp] += 1

for p1 in range(0, B):
    for p2 in range(p1+1, p1+B):
        tmp = sum(pizzaB[p1: p2])
        if tmp > N:
            break
        else:
            pizzaBcut[tmp] += 1

cnt = 0
for a1, a2 in pizzaAcut.items():
    if pizzaBcut[N-a1]:
        cnt += a2 * pizzaBcut[N-a1]
        # print(p1, p2)

print(cnt)