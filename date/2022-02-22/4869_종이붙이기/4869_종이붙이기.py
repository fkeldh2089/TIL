# 4869 종이 붙이기
import sys
sys.stdin = open('input_4869.txt')


def fac(n):  # 팩토리얼
    global memo
    if n >= 2 and len(memo) <= n:
        val = fac(n-1)*n
        memo.append(val)
    return memo[n]


TC = int(input())

# 스택을 써야하나?
for p in range(TC):
    N = int(input())
    N = N//10
    memo = [1, 1]
    ans = 0
    for q1 in range(N//2+1):  # q1는 20x20 의 개수
        for q2 in range(q1+1):  # q2 는 20x20중 2개 가로 구성
            c = q1 - q2
            b = q2
            a = N - 2*q1  # 10x20
            ans += fac(a+b+c)//(fac(a)*fac(b)*fac(c))
    if ans == 0:
        ans = 1
    print(f'#{p+1} {ans}')
