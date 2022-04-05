# 5185 이진수
import sys
sys.stdin = open('input_5185.txt')

TC = int(input())

for p in range(TC):
    n, num = input().split()
    n = int(n)
    tmp = bin(int(num, 16))
    tmp = tmp.replace('0b', '')
    if len(tmp) % 4:
        tmp = '0'*(4 - len(tmp) % 4) + tmp
    print(f'#{p+1} {tmp}')
