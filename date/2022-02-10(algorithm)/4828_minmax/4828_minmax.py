# 4828 min max
import sys
sys.stdin = open('input_4828.txt')

tc = int(input())

for p in range(tc):
    num = int(input())
    numbs = list(map(int, input().split()))
    max_num = numbs[0]
    min_num = numbs[0]

    for q in range(num): # 최소 최대값 구하기
        if numbs[q] >= max_num:
            max_num = numbs[q]
        if numbs[q] <= min_num:
            min_num = numbs[q]

    print(f'#{p+1} {max_num-min_num}')