# 5650 핀볼게임
import sys
from pprint import pprint
sys.stdin = open('input_5650.txt')

TC = int(input())
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
d1 = [1, 2, 3, 0]  # 각 삼각형 부딫히면 ~ -1 씩 해야함,,
d2 = [2, 0, 3, 1]
d3 = [3, 0, 1, 2]
d4 = [1, 3, 0, 2]
d5 = [1, 0, 3, 2]
ds = [d1, d2, d3, d4, d5]

for p in range(TC):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    holes = [[[-1, -1], [-1, -1]] for _ in range(5)]
    mn = 0  # 최소 수

    for q1 in range(N):
        for q2 in range(N):
            if field[q1][q2] >= 6:  # 웜홀 찾는 경우
                tmp = field[q1][q2] - 6
                if holes[tmp][0] == [-1, -1]:
                    holes[tmp][0] = [q1, q2]
                else:
                    holes[tmp][1] = [q1, q2]

    for q1 in range(N):
        for q2 in range(N):
            if field[q1][q2] == 0:
                for q3 in range(4):
                    pos_r, pos_c = q1, q2
                    d = q3  # 방향 설정
                    cnt = 0
                    while 1:
                        nr, nc = pos_r + dr[d], pos_c + dc[d]

                        if [nr, nc] == [q1, q2]:
                            break

                        if 0 <= nr < N and 0 <= nc < N:  # 장외 인가 아닌가,,
                            if field[nr][nc] == -1:  # 블랙홀 만나면 나오고,
                                break

                            if field[nr][nc] == 0:
                                d = d  # 방향 유지,
                                pos_r, pos_c = nr, nc  # 이동하고
                            else:
                                for s in range(1, 6):  # 블록에 대하여
                                    if field[nr][nc] == s:
                                        d = ds[s-1][d]  # 방향 전환
                                        pos_r, pos_c = nr, nc  # 이동하고
                                        cnt += 1  # 부딫힌 횟수 증가,
                                for s in range(6, 11):
                                    if field[nr][nc] == s:  # 웜홀에 대하여
                                        d = d  # 방향 유지,
                                        if [nr, nc] == holes[s-6][0]:
                                            pos_r, pos_c = holes[s-6][1]
                                        else:
                                            pos_r, pos_c = holes[s-6][0]

                        else:  # 벽에 부딫히면
                            d = d5[d]  # 방향 재설정
                            pos_r, pos_c = nr, nc
                            cnt += 1
                        # print(f'#[{pos_r},{pos_c}],{d} : {q1, q2}, {cnt}')
                    if cnt > mn:
                        mn = cnt
                    # print(f'#{p+1} {q1, q2},{q3} : {cnt}')
    print(f'#{p+1} {mn}')





