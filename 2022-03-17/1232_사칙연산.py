# 1232 사칙연산
import sys
sys.stdin = open('input_1232.txt')


def in_order(n):
    global nodes_nums, cnt
    if n:
        in_order(li1[n])
        in_order(li2[n])
        eq.append(nums[n - 1][1])


for p in range(10):
    N = int(input())
    nums = [list(input().split()) for _ in range(N)]
    # print(nums)
    li1 = [0] * (N + 1)
    li2 = [0] * (N + 1)
    eq = []
    for q in range(N):
        if len(nums[q]) == 4:
            li1[int(nums[q][0])] = int(nums[q][2])
            li2[int(nums[q][0])] = int(nums[q][3])
        elif len(nums[q]) == 3:
            li1[int(nums[q][0])] = int(nums[q][2])

    in_order(1)

    ans = []
    # print(eq)

    for q in eq:
        if q != '+' and q != '*' and q != '/' and q != '-':
            ans.append(int(q))
        elif q == '*':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a1 * a2)
        elif q == '+':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a1 + a2)
        elif q == '/':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a2/a1)
        elif q == '-':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a2-a1)

    ans1 = int(ans.pop())
    print(f'#{p+1} {ans1}')