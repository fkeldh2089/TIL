# 5188 최소합
import sys
sys.stdin = open('input_5188.txt')


def minsum(r, c, cnt):
    global mn
    if cnt > mn:
        return 0
    if 0 <= r < N and 0 <= c < N:
       cnt += mat[r][c]
    else:
        return 0
    if r == N-1 and c == N-1:
        # print(tmp)
        if mn > cnt:
            mn = cnt
            # print(tmp, mn)
        return 0
    if r+1<N:
        minsum(r+1, c, cnt)
    if c+1<N:
        minsum(r, c+1, cnt)


TC = int(input())
for p in range(TC):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    # print(mat)
    mn = 10000000000
    minsum(0, 0, 0)
    print(f'#{p+1} {mn}')
