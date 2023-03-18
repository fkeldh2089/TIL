# 10836 여왕벌
import sys
sys.stdin = open("input_10836.txt")

M, N = map(int, input().split())

rows = [0] *(2*M)
for p in range(N):
    inp = list(map(int, input().split()))
    idx = 0
    for p1 in range(2):
        idx += inp[p1]
        if idx>=0:
            rows[idx] += 1

rows[0] += 1
for p in range(1, 2*M):
    rows[p] += rows[p-1]

rep = ' '.join(list(map(str, rows[M:-1])))
for p in range(M-1, -1, -1):
    print(rows[p], end=" ")
    print(rep)