# Gravity
import sys
sys.stdin = open('input_Gravity.txt')

tc = int(input())
for p in range(tc):
    n = int(input())
    ob1 = list(map(int, input().split())) # 상자 적재 높이
    ob1_0 = ob1[::]
    maxnum = 0

    for q in range(n): # 모든 상자에 대하여
        cnt = 0
        for q1 in range(n-q): # 해당 상자열 보다 아래 있는 상자열에 대하여
            fallnum = 0
            if ob1[q] <= ob1[q+q1]: # 해당 상자보다 높은 상자열이 있다면 cnt +1
                cnt += 1
        fallnum = n - q -cnt # 해당 상자열의 위치에서 바닥의 높이를 빼고, 해당 상자보다 높은 상자열의 수만큼 뺴준다
        if maxnum <= (fallnum):
            maxnum = fallnum

    print(f'#{p+1} {maxnum}')
