import sys
sys.stdin = open("input.txt")

N = int(input())
field = []
for p in range(4):
    row = list(map(int, input().split()))
    field.append(row)
print(N, field)