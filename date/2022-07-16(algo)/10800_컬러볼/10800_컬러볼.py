# 10800_컬러볼
import sys
from collections import defaultdict
sys.stdin = open('input_10800.txt')

N = int(input())

balls = []
score = [0]*N
colors = defaultdict(int)
for p in range(N):
    balls.append(list(map(int, input().split()))+[p])

balls.sort(key=lambda x:x[1])
total_size = 0
tmp_size = 0
tmp = 0
idx = 0
for p in range(N):
    color, size, player = balls[p]
    while balls[idx][1] < balls[p][1]:
        color2, size2, player2 = balls[idx]
        total_size += size2
        colors[color2] += size2
        idx += 1
    score[player] += total_size - colors[color]
for p in range(N):
    print(score[p])