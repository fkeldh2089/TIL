# 5176 이진탐색
import sys
sys.stdin = open('input_5176.txt')


def in_order(n):
    global nodes_nums, cnt
    if n:
        in_order(li1[n])
        # print(n)
        cnt += 1
        nodes_nums[n] = cnt
        in_order(li2[n])



TC = int(input())

for p in range(TC):
    N = int(input())
    li1 = [0] * (N+1)
    li2 = [0] * (N+1)
    nodes_nums = [0] * (N + 1)
    for q in range(2, N+1):
        if li1[q//2] == 0:
            li1[q//2] = q
        else:
            li2[q//2] = q
    cnt = 0
    # print(li1)
    # print(li2)
    in_order(1)
    print(f'#{p+1} {nodes_nums[1]} {nodes_nums[N//2]}')