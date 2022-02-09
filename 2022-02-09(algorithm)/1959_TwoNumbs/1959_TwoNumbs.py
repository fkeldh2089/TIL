import sys

sys.stdin = open('input_1959.txt')

tc = int(input())

for p in range(tc):
    lalb = list(map(int, input().split()))
    numa = list(map(int, input().split()))
    numb = list(map(int, input().split()))

    la = lalb[0]
    lb = lalb[1]

    if la > lb:
        numb, numa = numa, numb
        la, lb = lb, la

    max_num = float('-inf')
    for q in range(lb - la + 1):
        numa_0 = [0]*q + numa + [0]*(lb - la -q) # 작은 쪽에 패딩
        temp_num = 0
        for q1 in range(lb):
            temp_num += numa_0[q1] * numb[q1]

        if max_num < temp_num:
             max_num = temp_num

    print(f'#{p+1} {max_num}')