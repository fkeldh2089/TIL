import sys
import math
sys.stdin = open('input_test.txt')

TC = int(input())

for p in range(TC):
    X, Y = list(map(int, input().split()))
    a = 12
    b = -4*(X+Y)
    c = X*Y/12
    h = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
    A = X - 2*h
    B = Y - 2*h
    sol = A*B*h
    print(h, sol)