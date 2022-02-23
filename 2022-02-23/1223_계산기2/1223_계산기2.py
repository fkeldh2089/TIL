# 1223 계산기 2
import sys
sys.stdin = open('input_1223.txt')

for p in range(10):
    N = int(input())
    cal = input()
    op = []
    nums = []
    for q in cal:
        if q != '+' and q != '*':  # 연산자 아니면 숫자로 변환
            nums.append(int(q))
        elif q == '*':  # *이 가장 높은 연산자
            op.append(q)
        elif q == '+':
            if len(op) == 0:
                op.append(q)
            else:
                if op[-1] == '+':
                    op.append(q)
                else:
                    while len(op) > 0 and op[-1] == '*':
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
    while op:
        nums.append(op.pop())

    ans = []
    for q in nums:
        if q != '+' and q != '*':
            ans.append(q)
        elif q == '*':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a1*a2)
        elif q == '+':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a1+a2)

    ans1 = ans.pop()
    print(f'#{p+1} {ans1}')
