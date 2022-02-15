# 2628 종이자르기
import sys
sys.stdin = open('input_2628.txt')


def sort_pill(N, nums):  # 버블 소트
    for q1 in range(N - 1):
        for q2 in range(N - q1 - 1):
            if nums[q2] > nums[q2 + 1]:
                nums[q2 + 1], nums[q2] = nums[q2], nums[q2 + 1]
    return nums


W, H = list(map(int, input().split()))  # 가로 세로 길이
N = int(input())  # 자를 횟수
x = [0]  # 세로 혹은 가로의 잘리는 지점 밑 끝점
y = [0]
cnt_x = 1
cnt_y = 1
for p in range(N):
    a, b = list(map(int, input().split()))
    if a == 0:
        x.append(b)
        cnt_x += 1
    else:
        y.append(b)
        cnt_y += 1
x = sort_pill(cnt_x, x)
y = sort_pill(cnt_y, y)
x. append(H)
y. append(W)

max1 = 0  # x와 y에서 잘리는 길이의 최대값
max2 = 0
for p in range(cnt_x):
    if max1 < x[-1-p] - x[-2-p]:
        max1 = x[-1-p] - x[-2-p]

for p in range(cnt_y):
    if max2 < y[-1-p] - y[-2-p]:
        max2 = y[-1-p] - y[-2-p]
ans = max1 * max2
print(ans)


