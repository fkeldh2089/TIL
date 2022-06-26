# 6190 정곤이의 단조 증가하는 수 real test input 늘려줘
import sys
sys.stdin = open('input_6190.txt')

TC = int(input())


def condan(n):
    k = n
    for q in range(len(str(n))-1):
        if n%10 < (n%100)//10:
            return -1
        n = n//10
    return k


def maxnum(a, b):
    if a >= b:
        return a
    else:
        return b


for p in range(TC):
    N = int(input())
    numbers1 = list(map(int, input().split()))
    numbers = []
    temp = 0

    ans = -1
    for q in range(N-1):
        for q1 in range(q+1, N):
            temp = numbers1[q] * numbers1[q1]
            temp = condan(temp)
            ans = maxnum(ans, temp)

    print(f'#{p+1} {ans}')



