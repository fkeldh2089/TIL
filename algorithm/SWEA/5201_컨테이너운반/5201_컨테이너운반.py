# 5201 컨테이너 운반
import sys
sys.stdin = open('input_5201.txt')

TC = int(input())
for p in range(TC):
    N, M = map(int, input().split())
    wn = list(map(int, input().split()))
    wm = list(map(int, input().split()))
    wn.sort(reverse=True)
    wm.sort(reverse=True)
    twice = [0]*N
    for q1 in range(M):
        for q2 in range(N):
            if wm[q1] >= wn[q2] and twice[q2] == 0:
                twice[q2] = 1
                break
    ans = 0
    for q in range(N):
        if twice[q] == 1:
            ans += wn[q]

    print(f'#{p+1} {ans}')
