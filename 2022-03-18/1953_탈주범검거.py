# 1953 탈주범 검거
import sys
from pprint import pprint
sys.stdin = open('input_1953.txt')
pipe_contanct = [
    [0],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1]
]


def run1():
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while pos:
        r, c = pos.pop(0)
        if twice[r][c] == T:
            break
        for p in range(4):
            nr, nc = r+dr[p], c+dc[p]
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] != 0 and twice[nr][nc] == 0:  # 빈칸이 아니라면,
                num1 = field[r][c]
                num2 = field[nr][nc]
                # print(num1, num2, (p+2)//4, pipe_contanct[num2][(p+2)//4])
                if pipe_contanct[num1][p]*pipe_contanct[num2][(p+2)%4]:
                    ans.append([nr, nc])
                    pos.append([nr, nc])
                    twice[nr][nc] = twice[r][c] + 1
                # pprint(twice)


TC = int(input())

for p in range(TC):
    # 전체 세로, 전체 가로, 가로 위치, 세로 위치, 시간
    N, M, R, C, T = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    twice = [[0 for _ in range(M)] for _ in range(N)]
    pos = [[R, C]]
    ans = [[R, C]]
    twice[R][C] = 1
    run1()
    print(f'#{p+1} {len(ans)}')


