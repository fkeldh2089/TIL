# 4466 최대 성적표
import sys
sys.stdin = open('input_4466.txt')

TC = int(input())


def sort(n, m):
    for p in range(n-1):
        for p1 in range(n-1):
            if m[p1] < m[p1+1]:
                m[p1], m[p1+1] = m[p1+1], m[p1]
    return m


for p in range(TC):
    N, K = list(map(int, input().split()))
    numbs = list(map(int, input().split()))
    sorted_numbs = sort(N, numbs)

    snum = 0
    for q in range(K):
        snum += sorted_numbs[q]

    print(f'{p+1} {snum}')

