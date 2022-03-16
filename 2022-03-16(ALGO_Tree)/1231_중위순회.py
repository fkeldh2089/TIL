# 1231 중위 순회
import sys
sys.stdin = open('input_1231.txt')


def in_order(v):
    if v:
        # if not ch1[v]:
        #     print(v)
        #     return
        # in_order(ch1[v])
        # print(v)
        # in_order(ch2[v])
        in_order(li1[v])
        print(nums[v-1][1], end='')
        in_order(li2[v])


for p in range(10):
    N = int(input())
    li1 = [0] * (N + 1)
    li2 = [0] * (N + 1)

    nums = [list(input().split()) for _ in range(N)]
    # print(nums)

    for q in range(N):
        if len(nums[q]) == 4:
            li1[int(nums[q][0])] = int(nums[q][2])
            li2[int(nums[q][0])] = int(nums[q][3])
        elif len(nums[q]) == 3:
            li1[int(nums[q][0])] = int(nums[q][2])

    print(f'#{p+1} ', end='')
    in_order(1)
    print()