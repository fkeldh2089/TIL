# 6019 기차 사이의 파리
import sys
sys.stdin = open('input_6019.txt')

TC = int(input())

for p in range(TC):
    L, A, B, F = list(map(int, input().split()))
    t = float(L/(B+A))
    print(f'#{p+1} {F*t:.6f}')