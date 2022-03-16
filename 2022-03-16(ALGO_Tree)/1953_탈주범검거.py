# 1953 탈주범 검거
import sys
sys.stdin = open('input_1953.txt')


def run():
    while T <= 0:
        r, c = pos.pop()
        twice[r][c] = 1
        if field[r][c] == 1:
            dr = [1, -1, 0, 0]
            dc = [0, 0, 1, -1]
            for p in range(4):
                nr, nc = r+dr[p], c+dc[p]
                if field[nr][nc] != 0:  # 빈칸이 아니라면,
                    pos.append(nr, nc)


TC = int(input())

for p in range(TC):
    # 전체 세로, 전체 가로, 가로 위치, 세로 위치, 시간
    N, M, R, C, T = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    twice = [[0 for _ in range(M)] for _ in range(N)]
    pos = [[R, C]]

