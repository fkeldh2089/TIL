# 5186 이진수 2
import sys
sys.stdin = open('input_5186.txt')

TC = int(input())
for p in range(TC):
    n = float(input())
    ans = ''
    for q in range(13):
        if n >= 1/(2**(q+1)):
            ans += '1'
            n -= 1/(2**(q+1))
        else:
            ans += '0'
        if n == 0:
            break
    else:
        ans = 'overflow'

    print(f'#{p+1} {ans}')