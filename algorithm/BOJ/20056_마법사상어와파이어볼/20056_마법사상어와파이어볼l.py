# 21610 마법사 상어와 파이어볼
import sys
sys.stdin = open('input_20056.txt')


def ball_move(d, s, now, N):  # d는 방향, s는 변위, now는 현재 위치, N은 필드 크기
    dir_r = [-1, -1, 0, 1, 1, 1, 0, -1]
    dir_c = [0, 1, 1, 1, 0, -1, -1, -1]
    new_pos = [now[0] + s*dir_r[d], now[1] + s*dir_c[d]]
    while not(0 <= new_pos[0] < N) or not(0 <= new_pos[1] < N):
        if new_pos[0] <= -1:
            new_pos[0] = N + new_pos[0]
        if new_pos[1] <= -1:
            new_pos[1] = N + new_pos[1]
        if new_pos[0] >= N:
            new_pos[0] = new_pos[0] - N
        if new_pos[1] >= N:
            new_pos[1] = new_pos[1] - N
    return new_pos


# N은 필드의 크기, M은 파이어볼 수, K는 이동 횟수
# r은 행, c는 열, m는 질량, s는 변위, d는 방향r, c, m, s, d
N, M, K = list(map(int, input().split()))
balls = [list(map(int, input().split())) for _ in range(M)]
for p in range(len(balls)):
    balls[p][0] -= 1
    balls[p][1] -= 1
for p in range(K):  # 이동은 K번
    field = [[[0, 0, 0, 0, 0] for _ in range(N)] for _ in range(N)]  # [개수, 질량, 속도, 방향, 방향 판단 기준]파이어볼 겹쳐지는 것 확인,
    ball_num = len(balls)  # 볼의 갯수
    for q in range(ball_num):
        r, c, m, s, d = balls[q]
        new_pos = ball_move(d, s, [r, c], N)
        field[new_pos[0]][new_pos[1]][0] += 1  # 갯수 증가
        field[new_pos[0]][new_pos[1]][1] += m  # 질량 증가
        field[new_pos[0]][new_pos[1]][2] += s  # 속도 증가
        field[new_pos[0]][new_pos[1]][3] += d  # 방향 증가
        field[new_pos[0]][new_pos[1]][4] += d % 2
    balls = []  # 파이어볼 정보 초기화
    for p1 in range(N):
        for p2 in range(N):
            if field[p1][p2][0] > 1:  # 파이어볼이 두 개 이상일 때
                if field[p1][p2][4] == 0 or field[p1][p2][4] == field[p1][p2][0]:  # 합쳐지는 방향이 모두 홀짝,
                    for q in range(0, 7, 2):   # 방향 0, 2, 4, 6
                        m1 = int(field[p1][p2][1]/5)  # 질량 / 5
                        if m1 == 0:  # 질량이 0 이면 안만듦
                            break
                        s1 = int(field[p1][p2][2]/field[p1][p2][0])  # 속력/ 갯수
                        d1 = q  # 방향
                        balls.append([p1, p2, m1, s1, d1])
                else:  # 합쳐지는 방향이 모두 홀짝이 아니면,
                    for q in range(1, 8, 2):   # 방향 1, 3, 5, 7
                        m1 = int(field[p1][p2][1]/5)  # 질량 / 5
                        if m1 == 0:  # 질량이 0 이면 안만듦
                            break
                        s1 = int(field[p1][p2][2]/field[p1][p2][0])  # 속력/ 갯수
                        d1 = q  # 방향
                        balls.append([p1, p2, m1, s1, d1])

            elif field[p1][p2][0] == 1:  # 파이어볼이 하나이면,
                m1 = field[p1][p2][1]
                s1 = field[p1][p2][2]
                d1 = field[p1][p2][3]
                balls.append([p1, p2, m1, s1, d1])

ans = 0
for p in range(len(balls)):
    ans += balls[p][2]
print(ans)

