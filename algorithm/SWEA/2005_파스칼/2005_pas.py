# 2005 파스칼의 삼각형
import sys
sys.stdin = open('input_2005.txt')


def pas(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        col = []
        for p in range(n):
            if p == 0 or p == n-1:
                col.append(1)
            else:
                col.append(pas(n-1)[p-1]+pas(n-1)[p])
        return col


def pas2(n):
    global memo
    if n >= 3 and len(memo) <= n:
        col = [0] * n  # n 만큼의 빈 공간을 만들고
        for r in range(n-1):
            col[r] += memo[n-2][r]
            col[r+1] += memo[n-2][r]
        memo.append(col)
    return memo[n-1]



TC = int(input())


for p in range(TC):
    memo = [[1], [1, 1]]
    N = int(input())
    N = N
    print(f'#{p+1}')
    for q in range(1, N+1):
        print(*pas2(q))