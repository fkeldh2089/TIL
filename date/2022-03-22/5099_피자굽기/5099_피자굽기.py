# 5099 피자 굽기
import sys
sys.stdin = open('input_5099.txt')

TC = int(input())

for p in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = []

    piz = [[0, 0, 0]]*N  # [몇 번 피자, 치즈, 시간]
    cnt = 1
    while 1:
        if nums:
            for q in range(N):
                if piz[q][0] == 0:
                    tmp_piz = nums.pop(0)
                    piz[q] = [cnt, tmp_piz, N]
                    cnt += 1
                    break

        for q in range(N):
            if piz[q][0] and piz[q][2] == 0:
                piz[q][1] = piz[q][1]//2
                if piz[q][1] == 0:
                    ans.append(piz[q][0])
                    piz[q] = [0, 0, 0]
                else:
                    piz[q][2] = N
        for q in range(N):
            if piz[q][2] > 0:
                piz[q][2] -= 1

        if len(ans) == M:
            break

    print(f'#{p+1} {ans[-1]}')
