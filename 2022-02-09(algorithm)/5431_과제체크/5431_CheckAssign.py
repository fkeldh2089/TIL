# 5431_민석이의 과제 체크하기
import sys

sys.stdin = open('input_5431.txt')

tc = int(input())

for p in range(tc):
    N_K = list(map(int, input().split()))
    nums = N_K[0]
    submit_num = N_K[1]
    submits = list(map(int, input().split()))
    people = [0]*nums # 체크용

    #print(submits)
    for q in range(submit_num):
        people[submits[q] - 1] = 1

    no_sub = []
    for q in range(nums):
        if people[q] == 0:
            no_sub.append(q+1)

    ans = ' '.join(list(map(str,no_sub)))
    print(f'#{p+1} {ans}')