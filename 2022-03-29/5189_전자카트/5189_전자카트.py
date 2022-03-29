# 5189 전자카트
import sys
sys.stdin = open('input_5189.txt')
from itertools import permutations


TC = int(input())
for p in range(TC):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    mn = 100000
    nums = list(range(1, N+1))
    for q in permutations(nums, N):
        print(q)
        cnt = mat[q[-1]-1][q[0]-1]
        for q1 in range(N-1):
            cnt += mat[q[q1]-1][q[q1+1]-1]
            if cnt > mn:
                break
        if mn > cnt:
            mn = cnt
    print(f'#{p+1} {mn}')