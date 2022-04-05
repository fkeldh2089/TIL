# 17144 dust
import sys
from pprint import pprint
sys.stdin = open('input_17144.txt')
input = sys.stdin.readline


def dust_move(mat):  # 시간 초과
    global dr, dc, R, C
    dust = []
    for q1 in range(R):
        for q2 in range(C):
            if mat[q1][q2] > 0:
                dust.append([q1, q2, mat[q1][q2]])
    for q in dust:
        pos = q[0:2]
        mass = q[2]
        for r in range(4):
            new_pos = [pos[0] + dr[r], pos[1] + dc[r]]
            if 0 <= new_pos[0] < R and 0 <= new_pos[1] < C and mat[new_pos[0]][new_pos[1]] != -1:
                mat[new_pos[0]][new_pos[1]] += mass//5
                mat[pos[0]][pos[1]] -= mass//5
    return mat


def dust_move2():  # 시간 초과
    global dr, dc, R, C
    dust = []
    for q1 in range(R):
        for q2 in range(C):
            if field[q1][q2] > 0:
                dust.append([q1, q2, field[q1][q2]])
    for q in dust:
        pos = q[0:2]
        mass = q[2]
        for r in range(4):
            new_pos = [pos[0] + dr[r], pos[1] + dc[r]]
            if 0 <= new_pos[0] < R and 0 <= new_pos[1] < C and field[new_pos[0]][new_pos[1]] != -1:
                field[new_pos[0]][new_pos[1]] += mass//5
                field[pos[0]][pos[1]] -= mass//5


def dust_move3():
    tmp_field = [[0] * C for _ in range(R)]
    for q1 in range(R):
        for q2 in range(C):
            if field[q1][q2] > 0:
                tmp = 0
                for r in range(4):
                    nx, ny = q1 + dr1[r], q2 + dc1[r]
                    if 0 <= nx < R and 0 <= ny < C and field[nx][ny] != -1:
                        tmp_field[nx][ny] += field[q1][q2] // 5
                        tmp += field[q1][q2] // 5
                field[q1][q2] -= tmp
    for q1 in range(R):
        for q2 in range(C):
            field[q1][q2] += tmp_field[q1][q2]


def wind(mat, air):
    ri1 = mat[air][1:-1]
    ri2 = mat[air + 1][1:-1]
    up1 = list(map(list, zip(*mat)))[-1][1:air+1]
    up2 = list(map(list, zip(*mat)))[-1][-2:air:-1]
    le1 = mat[0][1:]
    le2 = mat[-1][1:]
    do1 = list(map(list, zip(*mat)))[0][0:air-1]
    do2 = list(map(list, zip(*mat)))[0][-1:air+2:-1]
    # 공기청정기 오른쪽으로,,
    mat[air] = [-1, 0] + ri1
    mat[air + 1] = [-1, 0] + ri2
    # 위쪽으로
    for q in range(len(up1)):
        mat[q][-1] = up1[q]
    for q in range(len(up2)):
        mat[-1-q][-1] = up2[q]
    # 왼쪽으로,,
    mat[0][0:-1] = le1
    mat[-1][0:-1] = le2
    # 아래로,,
    for q in range(len(do1)):
        mat[q+1][0] = do1[q]
    for q in range(len(do2)):
        mat[-2-q][0] = do2[q]

    return mat


def wind2():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    d = 0
    dust_o = 0  # 전 칸 먼지 값
    pos_x, pos_y = air1, 1  # 위쪽 공기 청정기 오른쪽 방향으로 시작
    while 1:
        nx = pos_x + dr[d]
        ny = pos_y + dc[d]
        if pos_x == air1 and pos_y == 0:  # 공기청정기로 돌아온 경우,
            break
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            d += 1
            continue
        field[pos_x][pos_y], dust_o = dust_o, field[pos_x][pos_y]
        pos_x = nx
        pos_y = ny


def wind3():
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    d = 0
    dust_o = 0  # 전 칸 먼지 값
    pos_x, pos_y = air1 + 1, 1  # 아래쪽 공기 청정기 오른쪽 방향으로 시작
    while 1:
        nx = pos_x + dr[d]
        ny = pos_y + dc[d]
        if pos_x == air1 + 1 and pos_y == 0:  # 공기청정기로 돌아온 경우,
            break
        if nx >= R or nx < 0 or ny >= C or ny < 0:
            d += 1
            continue
        field[pos_x][pos_y], dust_o = dust_o, field[pos_x][pos_y]
        pos_x = nx
        pos_y = ny


R, C, T = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(R)]
for p in range(R):
    if field[p][0] == -1:
        air1 = p
        break

dr1 = [1, -1, 0, 0]
dc1 = [0, 0, -1, 1]
for p in range(T):
    dust_move3()
    wind2()
    wind3()

tmp_sum = 2
for p1 in range(R):
    for p2 in range(C):
        tmp_sum += field[p1][p2]

print(tmp_sum)


