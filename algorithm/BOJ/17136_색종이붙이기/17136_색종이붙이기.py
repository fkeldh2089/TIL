# 17136 색종이 붙이기
import sys
from pprint import pprint
sys.stdin = open('input_17136.txt')


def DFS(r, c, paper, cnt):
    global mn
    if 10 <= c:
        r += 1
        c = 0
    if 10 <= r:
        if cnt < mn:
            # print(paper, cnt)
            mn = cnt
        return
    if mat[r][c] == 1:
        for q in range(1, 6):
            nr = r+q
            nc = c+q
            if paper[q] > 4:
                continue
            if nr > 10 or nc > 10:
                continue
            f = 0
            for q1 in range(r, nr):
                for q2 in range(c, nc):
                    if mat[q1][q2] == 0:
                        f = 1
                        break
                if f == 1:
                    break
            else:
                for q1 in range(r, nr):
                    for q2 in range(c, nc):
                        mat[q1][q2] = 0
                paper[q] += 1
                # print(paper, cnt)
                # pprint(mat)
                DFS(r, nc, paper, cnt+1)
                paper[q] -= 1
                for q1 in range(r, nr):
                    for q2 in range(c, nc):
                        mat[q1][q2] = 1

    elif mat[r][c] == 0:
        DFS(r, c+1, paper, cnt)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

mat = [list(map(int, input().split())) for _ in range(10)]
ans = 0
mn = 50
paper = [0]*6
DFS(0, 0, paper, 0)
# print(paper)
if mn == 50:
    mn = -1
print(mn)