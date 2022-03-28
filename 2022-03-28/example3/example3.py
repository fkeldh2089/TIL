import sys
sys.stdin = open('input_ex3.txt')

TC = int(input())
for p in range(TC):
    nums = list(map(int, input().split()))
    l = len(nums)
    print(f'#{p + 1} ', end='')
    for q in range(2**l):
        tmp = []
        for q1 in range(l):
            if q & (1<<q1):
                tmp.append(nums[q1])
        sum_num = 0
        for q1 in range(len(tmp)):
            sum_num += tmp[q1]
        if sum_num == 10:
            print(tmp,end='')

    print()