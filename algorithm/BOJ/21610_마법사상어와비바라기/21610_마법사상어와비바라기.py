# 21610 마법사 상어와 비바라기
import sys
sys.stdin = open('input_21610.txt')


def cloud_move(ds, n, F):  # d는 방향인자, n[r, c]은 구름의 초기좌표, F은 필드의 크기(N)
    dir_r = [0, -1, -1, -1, 0, 1, 1, 1]
    dir_c = [-1, -1, 0, 1, 1, 1, 0, -1]
    pos = n
    d = ds[0] - 1  # 방향
    s = ds[1]  # 변위
    new_pos = [pos[0] + s*dir_r[d], pos[1] + s*dir_c[d]]
    while not(0 <= new_pos[0] < F) or not(0 <= new_pos[1] < F):
        if new_pos[0] <= -1:
            new_pos[0] = F + new_pos[0]
        if new_pos[1] <= -1:
            new_pos[1] = F + new_pos[1]
        if new_pos[0] >= F:
            new_pos[0] = new_pos[0] - F
        if new_pos[1] >= F:
            new_pos[1] = new_pos[1] - F
    return new_pos


def copy_water(n, F, F_n):  # n은 구름의 좌표, F는 필드에 있는 물량, F_n은 필드의 크기(N)
    dir_r = [-1, -1, 1, 1]
    dir_c = [-1, 1, 1, -1]
    pos = n
    cnt = 0  # 물 카운트
    for p in range(4):  # 대각선 4방향에 대하여
        new_pos = [pos[0] + dir_r[p], pos[1] + dir_c[p]]
        if (0 <= new_pos[0] < F_n) and (0 <= new_pos[1] < F_n):  # 대각선이 필드안에 있다면
            if F[new_pos[0]][new_pos[1]] >= 1:  # 물이 있다면
                F[pos[0]][pos[1]] += 1  # 물이 증가한다
                cnt += 1
    return [F, cnt]


# N은 필드 크기, M은 구름의 이동
N, M = list(map(int, input().split()))
field = [list(map(int, input().split())) for _ in range(N)]
dir_r = [0, -1, -1, -1, 0, 1, 1, 1]
dir_c = [-1, -1, 0, 1, 1, 1, 0, -1]
now = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]  # 구름의 초기 좌표
mkc = [[0]*N for _ in range(N)]  # 다음 구름 후보 좌표
water = 0
for p1 in range(N):
    for p2 in range(N):
        water += field[p1][p2]  # 전체 물
        if field[p1][p2] >= 2:  # 물이 2이상인 부분 좌표
            mkc[p1][p2] = 1

for p in range(M):  # 이동 횟수만큼 반복하는 비바라기
    cloud_count = len(now)  # 구름의 수
    clouds = []
    twice = [[0]*N for _ in range(N)]  # in 을 안써보자,,
    Move = list(map(int, input().split()))
    for q in range(cloud_count):  # 구름 수 만큼 반복
        pos = now[q]
        new_pos = cloud_move(Move, pos, N)
        field[new_pos[0]][new_pos[1]] += 1
        water += 1
        clouds.append(new_pos)
        twice[new_pos[0]][new_pos[1]] = 1

    for q in range(cloud_count):
        field, water_plus = copy_water(clouds[q], field, N)
        water += water_plus
        if field[clouds[q][0]][clouds[q][1]] >= 2:
            mkc[clouds[q][0]][clouds[q][1]] = 1

    now = []  # now 초기화
    dry = []  # 물이 적어진 곳
    for p1 in range(N):
        for p2 in range(N):
            if mkc[p1][p2] == 1 and twice[p1][p2] == 0:
                now.append([p1, p2])
                field[p1][p2] -= 2
                water -= 2
                if field[p1][p2] < 2:  # 2보다 물이 적어졌으면
                    mkc[p1][p2] = 0

print(water)