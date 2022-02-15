# 10163 색종이
import sys
sys.stdin = open('input_10163.txt')

N = int(input())  # 색종이 수
field = [[0]*1001 for _ in range(1001)]
for p in range(N):
    # X: 시작 좌표 Y: 시작 좌표 W: 너비 H: 높이
    X, Y, W, H = list(map(int, input().split()))
    for q1 in range(X, X + W):
        field[q1][Y:Y+H] = [p + 1] * H

cnt = [0] * (N + 1)
for p1 in range(1001):
    for p2 in range(1001):
        cnt[field[p1][p2]] += 1

for p in range(1, N+1):
    print(cnt[p])