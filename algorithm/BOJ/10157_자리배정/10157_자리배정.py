# 10157 자리배정
import sys
sys.stdin = open('input_10157.txt')

N, K = list(map(int, input().split()))  # 좌석 수
Ob = int(input())  # 좌석 위치
house = [[0] * K for _ in range(N)]  # 빈 달팽이 집

# 시작 위치, 문제 상 pos = (po_x, po_y)
po_x = 0
po_y = 0
if Ob <= N*K:
    f = 0
    for q in range(Ob - 1):  # 길가면서 채워준다는 느낌
        house[po_x][po_y] = q + 1  # 일단 채우고
        if f == 0:
            if (po_y + 1 < K) and (house[po_x][po_y + 1] == 0):  # 오른쪽이 0이면,,
                po_y += 1
            elif (po_x + 1 < N) and house[po_x + 1][po_y] == 0:  # 아래가 0이 아니라면,
                po_x += 1
            elif (po_y - 1 >= 0) and house[po_x][po_y - 1] == 0:  # 왼쪽이 0이 아니라면,
                po_y -= 1
                f = 1
            else:
                po_x -= 1
        else:
            if (po_y + 1 >= 0) and house[po_x][po_y - 1] == 0:  # 왼쪽이 0이 아니라면,
                po_y -= 1
            elif (po_x - 1 >= 0) and house[po_x - 1][po_y] == 0:  # 아래가 0이 아니라면,
                po_x -= 1
            elif (po_y + 1 < K) and (house[po_x][po_y + 1] == 0):  # 오른쪽이 0이면,,
                po_y += 1
                f = 0
            else:
                po_x += 1
    print(po_x + 1, po_y + 1)

else:
    print(0)
