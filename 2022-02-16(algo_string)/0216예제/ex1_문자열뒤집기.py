# 연습문제 1 문자열 뒤집기
import sys
sys.stdin = open('input_ex1.txt')

TC = int(input())
for p in range(TC):
    moon_ja = input()
    ans = ''.join(list(reversed(moon_ja)))
    print(f'#{p+1} {ans}')

# for p in range(TC):
#     moon_ja = input()
#     ans = moon_ja[::-1]
#     print(f'#{p+1} {ans}')
