# 5207 이진 탐색
import sys
sys.stdin = open('input_5207.txt')

TC = int(input())
for p in range(TC):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    cnt = 0
    for q in range(M):
        l, r = 0, N - 1

        f = 0
        while 1:
            mid = (l + r) // 2
            if A[mid] > B[q]:
                r = mid - 1
                if f == 1:
                    break
                f = 1

            elif A[mid] < B[q]:
                l = mid + 1
                if f == 2:
                    break
                f = 2

            elif A[mid] == B[q]:
                cnt += 1
                break

            if l > r:
                break
    print(f'#{p+1} {cnt}')
