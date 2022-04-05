# 연구소
import sys
from pprint import pprint
sys.stdin = open('input_lab.txt')
from collections import deque
from copy import deepcopy


def virus(field):  # 전염
    global mn
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    twice = [[0]*M for _ in range(N)]  # 중복 방지
    max_num = 0
    for p1 in range(N):  # 모든 좌표에 대하여
        for p2 in range(M):
            if twice[p1][p2] == 0 and field[p1][p2] == 2:
                rooms = deque()
                now_pos = [p1, p2]
                rooms.append(now_pos)
                twice[p1][p2] = 1
                idx1 = 0
                while 1:  # 길이 끊길 때 까지 반복
                    idx = idx1
                    idx1 = len(rooms)
                    for r in range(idx, len(rooms)):
                        for p in range(4):  # 4가지 방향에 대하여
                            new_pos = [dr[p] + rooms[r][0], dc[p] + rooms[r][1]]
                            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < M:  # 필드 범위안에 들어가고
                                if field[new_pos[0]][new_pos[1]] == 0 and twice[new_pos[0]][new_pos[1]] == 0:  # 통로
                                    rooms.append(new_pos)  # rooms에 추가
                                    twice[new_pos[0]][new_pos[1]] = 1
                    if len(rooms) == idx1:  # rooms 수가 증가하지 않았다면, break
                        break
                max_num += idx1
        # pprint(twice)
        # pprint(field)
    if max_num < mn:
        mn = max_num


def pil():

    for p1 in range(len(pillars)):
        tmp_field1 = deepcopy(field)
        tmp_field1[pillars[p1][0]][pillars[p1][1]] = 1
        for p2 in range(p1+1, len(pillars)):
            tmp_field2 = deepcopy(tmp_field1)
            tmp_field2[pillars[p2][0]][pillars[p2][1]] = 1
            for p3 in range(p2+1, len(pillars)):
                tmp_field3 = deepcopy(tmp_field2)
                tmp_field3[pillars[p3][0]][pillars[p3][1]] = 1
                virus(tmp_field3)


N, M = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
pillars = []
mn = N*M
cnt1 = 3
for q1 in range(N):
    for q2 in range(M):
        if field[q1][q2] == 0:
            pillars.append([q1, q2])
        if field[q1][q2] == 1:
            cnt1 += 1

pil()
print(M*N - cnt1 - mn)