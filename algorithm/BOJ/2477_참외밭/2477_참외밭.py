# 2477 참외밭
import sys
sys.stdin = open('input_2477.txt')

N = int(input())  # 참외 개수
lines = [list(map(int, input().split())) for _ in range(6)]
# 큰 사각에서 작은 사각을 빼는 느낌으로
# 큰 사각
direction = [0]*4
for p in range(6):  # 방향의 개수를 확인 1개 있는 것이 큰 사각
    direction[lines[p][0] - 1] += 1

big_line = []
for p in range(4):
    if direction[p] == 1:
        big_line.append(p+1)

for p in range(6):
    for q in range(2):
        if big_line[q] == lines[p][0]:  # 방향이 같으면
            big_line.append(lines[p][1])  # 길이를 추가
big_area = big_line[2] * big_line[3]

# 작은 사각
small_line = []
for p in range(5):
    if lines[p+1][0] != big_line[0] and lines[p+1][0] != big_line[1]:  # 멀쩡한 선분에 이웃하지 않은 경우
        if lines[p-1][0] != big_line[0] and lines[p-1][0] != big_line[1]:
            small_line.append(lines[p][1])
if len(small_line) == 1:
    small_line.append(lines[5][1])
small_area = small_line[0] * small_line[1]

print((big_area - small_area)*N)
