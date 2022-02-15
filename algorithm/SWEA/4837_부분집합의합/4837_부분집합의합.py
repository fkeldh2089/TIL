# 4837 부분집합의 합
import sys
sys.stdin = open('input_4837.txt')

tc = int(input())
for p in range(tc):
    # N 부분집합의 수, K 목표 합
    N, K = list(map(int, input().split()))

    arr = range(1, 13)
    cnt = 0  # 조건에 맞는 부분집합 갯수
    for q in range(1 << 12):
        tmp = 0  # 부분집합의 합
        par = 0  # 부분집합 원소의 갯수
        for q1 in range(12):
            if q & (1 << q1):
                tmp += arr[q1]
                par += 1
        #print(par, tmp)
        if tmp == K and par == N:
            cnt += 1

    print(f'#{p+1} {cnt}')


