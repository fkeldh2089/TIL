# 10158 개미
import sys
sys.stdin = open('input_10158.txt')

W, H = list(map(int, input().split()))  # 격자
X, Y = list(map(int, input().split()))  # 초기 위치
t = int(input())

x = X + t  # 그냥 평면에 쫙 펼쳐 버려
y = Y + t

x1 = x//W
x2 = x % W
y1 = y//H
y2 = y % H

if x1 % 2:
    x = W - x2
else:
    x = x2

if y1 % 2:
    y = H - y2
else:
    y = y2

print(x, y)




# y = Y  # 델타 풀이 시간 초과
# x = X
# f = 0
# dx = [1, -1]
# dy = [1, -1]
# d1 = 0  # 방향인자
# d2 = 0
#
# for q in range(t):
#     while(1):
#         nx = x + dx[d1]
#         ny = y + dy[d2]
#
#         if 0 <= nx <= W and 0 <= ny <= H:
#             x = nx
#             y = ny
#             break
#         else:
#             if not (0 <= nx <= W):
#                 d1 += 1
#                 d1 = d1 % 2
#             if not (0 <= ny <= H):
#                 d2 += 1
#                 d2 = d2 % 2
# print(x, y)

# for q in range(t):  # 길가면서 채워준다는 느낌 실행시간 초과
#     if f == 0:
#         if po_x + 1 <= W and po_y + 1 <= H:
#             po_x += 1
#             po_y += 1
#             f = 0
#         elif po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 1
#         elif po_x - 1 >= 0 and po_y - 1 >= 0:
#             po_x -= 1
#             po_y -= 1
#             f = 2
#         elif po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 3
#     elif f == 1:
#         if po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 1
#         elif po_x - 1 >= 0 and po_y - 1 >= 0:
#             po_x -= 1
#             po_y -= 1
#             f = 2
#         elif po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 3
#         elif po_x + 1 <= W and po_y + 1 <= H:
#             po_x += 1
#             po_y += 1
#             f = 0
#     elif f == 2:
#         if po_x - 1 >= 0 and po_y - 1 >= 0:
#             po_x -= 1
#             po_y -= 1
#             f = 2
#         elif po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 3
#         elif po_x + 1 <= W and po_y + 1 <= H:
#             po_x += 1
#             po_y += 1
#             f = 0
#         elif po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 1
#     elif f == 3:
#         if po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 3
#         elif po_x + 1 <= W and po_y + 1 <= H:
#             po_x += 1
#             po_y += 1
#             f = 0
#         elif po_x - 1 >= 0 and po_y + 1 <= H:
#             po_x -= 1
#             po_y += 1
#             f = 1
#         elif po_x - 1 >= 0 and po_y - 1 >= 0:
#             po_x -= 1
#             po_y -= 1
#             f = 2
# print(po_x, po_y)