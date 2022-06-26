import sys
sys.stdin = open('input_ex1.txt')


def SelectionSort(N, n):
    mn = 100000

    for q in range(len(N)-n):
        if N[n+q] <= mn:
            mn = N[n+q]
            tmp = n+q
    N[n], N[tmp] = mn, N[n]

    if len(N)-1 == n:
        return 0
    n += 1
    SelectionSort(N, n)



TC = int(input())

for p in range(TC):
    N = list(map(int, input().split()))
    SelectionSort(N, 0)
    print(N)