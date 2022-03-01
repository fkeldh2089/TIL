# 20057 마법사 상어와 토네이도
import sys
sys.stdin = open('input_20057.txt')


def make_root(N):  # 델타함수를 이용하는 것보다, index를 이용하는 것이 시간이 짧을 듯?
    house = [[0]*N for _ in range(N)]  # 빈 달팽이 집
    for q in range(N):
        house[0][q] = q + 1  # 첫째줄 채워주고
    pos = [0, N-1]  # 시작 위치
    cnt = N
    for q in range(N - 1):  # 길가면서 채워준다는 느낌
        if q % 2 == 0:
            for q1 in range(N-1-q):
                pos[0] += 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt
            for q1 in range(N-1-q):
                pos[1] -= 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt

        else:
            for q1 in range(N-1-q):
                pos[0] -= 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt
            for q1 in range(N-1-q):
                pos[1] += 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt
    return house


def find_root(N, house, now_pos):  # 토네이도의 다음 위치
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    for p in range(4):
        new_pos = [dr[p] + now_pos[0], dc[p] + now_pos[1]]
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:
            if house[new_pos[0]][new_pos[1]] == house[now_pos[0]][now_pos[1]] - 1:
                return [new_pos, p]


def wind_sand(N, field, now_pos, to_dir):  # 토네이도의 작용
    dr = [-2, -1, -1, -1, 0, 0, 1, 1, 1, 2]
    dc = [0, -1, 0, 1, -2, -1, -1, 0, 1, 0]

    wind = [2, 10, 7, 1, 5, 0, 10, 7, 1, 2]
    dust = field[now_pos[0]][now_pos[1]]  # 모래의 양
    field_out = 0  # 장외 모래의 양
    field[now_pos[0]][now_pos[1]] = 0  # 모래의 양 초기화,
    dust_sum = 0
    if to_dir == 0:  # 왼쪽으로 가는 경우
        for p in range(10):
            new_pos = [dr[p] + now_pos[0], dc[p] + now_pos[1]]
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
                field[new_pos[0]][new_pos[1]] += (dust * wind[p])//100
                dust_sum += (dust * wind[p])//100
            else:
                field_out += (dust * wind[p])//100
                dust_sum += (dust * wind[p]) // 100
        new_pos = [dr[5] + now_pos[0], dc[5] + now_pos[1]]
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
            field[new_pos[0]][new_pos[1]] += dust - dust_sum
        else:
            field_out += dust - dust_sum

    elif to_dir == 1:  # 아래로 향할 경우
        for p in range(10):
            new_pos = [-dc[p] + now_pos[0], dr[p] + now_pos[1]]
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
                field[new_pos[0]][new_pos[1]] += (dust * wind[p])//100
                dust_sum += (dust * wind[p]) // 100
            else:
                field_out += (dust * wind[p])//100
                dust_sum += (dust * wind[p]) // 100
        new_pos = [-dc[5] + now_pos[0], dr[5] + now_pos[1]]
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
            field[new_pos[0]][new_pos[1]] += dust - dust_sum
        else:
            field_out += dust - dust_sum

    elif to_dir == 2:  # 오른쪽으로 향할 경우(180deg 회전)
        for p in range(10):
            new_pos = [-dr[p] + now_pos[0], -dc[p] + now_pos[1]]
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
                field[new_pos[0]][new_pos[1]] += (dust * wind[p]) // 100
                dust_sum += (dust * wind[p]) // 100
            else:
                field_out += (dust * wind[p]) // 100
                dust_sum += (dust * wind[p]) // 100
        new_pos = [-dr[5] + now_pos[0], -dc[5] + now_pos[1]]
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
            field[new_pos[0]][new_pos[1]] += dust - dust_sum
        else:
            field_out += dust - dust_sum

    elif to_dir == 3:  # 위로 향할 때
        for p in range(10):
            new_pos = [dc[p] + now_pos[0], dr[p] + now_pos[1]]
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
                field[new_pos[0]][new_pos[1]] += (dust * wind[p])//100
                dust_sum += (dust * wind[p]) // 100
            else:
                field_out += (dust * wind[p])//100
                dust_sum += (dust * wind[p]) // 100
        new_pos = [dc[5] + now_pos[0], dr[5] + now_pos[1]]
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:  # 범위 안에 들어가면,
            field[new_pos[0]][new_pos[1]] += dust - dust_sum
        else:
            field_out += dust - dust_sum

    return [field, field_out]


N = int(input())  # 필드의 크기
field = [list(map(int, input().split())) for _ in range(N)]
house = make_root(N)
tornado = [N//2, N//2]  # 토네이도의 초기 위치
# de_sand = 0
# sand = 0
ans = 0
# for p1 in range(N):
#     for p2 in range(N):
#         de_sand += field[p1][p2]

for p in range(N**2-1):
    tornado, to_dir = find_root(N, house, tornado)  # 토네이도의 다음 위치
    field, sand_plus = wind_sand(N, field, tornado, to_dir)
    ans += sand_plus
# for p1 in range(N):
#     for p2 in range(N):
#         sand += field[p1][p2]

print(ans)


