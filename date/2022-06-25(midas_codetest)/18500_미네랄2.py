import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input_18500.txt')


def BFS(r, c):
    # print(r, c)
    if not (0<=r<R and 0<=c<C):
        return
    # print(field[r][c])
    if field[r][c] != 'x':
        return
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    q = deque([[r, c]])
    mn = R
    visited = [[0]*C for _ in range(R)]
    block = [[r, c]]
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0<=nr<R and 0<=nc<C and visited[nr][nc]==0:
                tmp = 0
                visited[nr][nc] = 1
                if field[nr][nc] == 'x':
                    if nr == R - 1:
                        return
                    block.append([nr, nc])
                    q.append([nr, nc])
                    # pprint(field)
                    for p in range(1, R-nr):
                        # print(field[nr+p][nc], nr+p, nc)
                        if field[nr+p][nc] == '.':
                            tmp += 1
                        elif visited[nr+p][nc]:
                            tmp = 0
                            break
                        else:
                            break
                    # print(f'tmp: {tmp}')
                    if mn > tmp and tmp:
                        mn = tmp
        # print(q, r, c, mn)

    if len(block) == 1:
        nr, nc = block[0]
        tmp = 0
        for p in range(1, R - nr):
            # print(field[nr+p][nc], nr+p, nc)
            if field[nr + p][nc] == '.':
                tmp += 1
            elif visited[nr + p][nc]:
                tmp = 0
                break
            else:
                break
        # print(f'tmp: {tmp}')
        if mn > tmp and tmp:
            mn = tmp
    falling(mn, block)
    return [mn, block]


def falling(mn, block):
    # print(mn, block)
    # pprint(field)
    for p in block:
        r, c = p
        if field[r+mn][c] != 'o':
            field[r][c] = '.'
            field[r+mn][c] = 'o'
    # pprint(field)

R, C = map(int, input().split())
field = [list(input()) for _ in range(R)]
N = int(input())
throw = list(map(int, input().split()))
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
# print(field)
f = 1
for p in range(N):
    floor = (R-throw[p])
    # print(R, throw[p])
    # print(f' floor: {floor}')
    falls = []
    if f == 1:
        for q in range(C):
            if field[floor][q] == 'x':
                field[floor][q] = '.'
                for d in range(4):
                    # print(field[floor+dr[d]][q+dc[d]])
                    tmp = BFS(floor+dr[d], q+dc[d])
                    if tmp:
                        falls.append(tmp)
                break
        f = 0
    else:
        for q in range(C):
            if field[floor][-q-1] == 'x':
                field[floor][-1-q] = '.'
                for d in range(4):
                    tmp = BFS(floor+dr[d], C-q-1+dc[d])
                    if tmp:
                        falls.append(tmp)
                break
        f = 1
    for q1 in range(R):
        for q2 in range(C):
            if field[q1][q2] == 'o':
                field[q1][q2] = 'x'

    # pprint(field)
for p in field:
    print(''.join(p))