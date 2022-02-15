# 2564 경비원
import sys
sys.stdin = open('input_2564.txt')

W, H = list(map(int, input().split()))  # 가로 세로
N = int(input())  # 상가의 개수
nums = [list(map(int, input().split())) for _ in range(N)]  # 위치
pos = list(map(int, input().split()))  # 본인 위치

dx = [0, 0, 0, 0, W]  # 왼쪽 아래 모서리를 기준으로 좌표로 계산
dy = [0, H, 0, 0, 0]

if pos[0] < 3:
    pos_n = [dx[pos[0]] + pos[1], dy[pos[0]]]
else:
    pos_n = [dx[pos[0]], dy[pos[0]] + (H - pos[1])]

tmp_sum = 0
for p in range(N):
    if nums[p][0] < 3:
        num_n = [dx[nums[p][0]] + nums[p][1], dy[nums[p][0]]]
    else:
        num_n = [dx[nums[p][0]], dy[nums[p][0]] + (H - nums[p][1])]
    if pos[0] + nums[p][0] == 3 or pos[0] + nums[p][0] == 7:
        if pos_n[0] + num_n[0] > (2*W -(pos_n[0] + num_n[0])):
            tmp_sum += abs(num_n[1]-pos_n[1]) + (2*W -(pos_n[0] + num_n[0]))
        else:
            tmp_sum += abs(num_n[1] - pos_n[1]) + pos_n[0] + num_n[0]
    else:
        tmp_sum += abs(num_n[0]-pos_n[0]) + abs(num_n[1]-pos_n[1])

print(tmp_sum)
