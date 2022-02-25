# 1224 계산기3
import sys
sys.stdin = open('input_1224.txt')

pri = {'(': -1, '+': 0, '-': 0, '*': 1, '/': 1, ')': -2}

for p in range(10):
    N = int(input())
    eq = input()
    nums = []
    op = []
    for q in eq:
        if q != '+' and q != '*' and q != '/' and q != '-' and q != ')' and q != '(':  # 연산자 아니면 숫자로 변환
            nums.append(int(q))
        elif q == '(':
            op.append(q)
        elif q == '*':  # *이 가장 높은 연산자
            if len(op) == 0:
                op.append(q)
            else:
                if op[-1] == '*':
                    op.append(q)
                else:
                    while len(op) > 0 and op[-1] == '/':
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
        elif q == '/':
            if len(op) == 0:
                op.append(q)
            else:
                if op[-1] == '/':
                    op.append(q)
                else:
                    while len(op) > 0 and op[-1] == '*':
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
        elif q == '+':
            if len(op) == 0:
                op.append(q)
            else:
                if op[-1] == '+':
                    op.append(q)
                else:
                    while len(op) > 0 and (op[-1] == '*' or op[-1] == '/' or op[-1] == '-'):
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
        elif q == '-':
            if len(op) == 0:
                op.append(q)
            else:
                if op[-1] == '-':
                    op.append(q)
                else:
                    while len(op) > 0 and (op[-1] == '*' or op[-1] == '/' or op[-1] == '+'):
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
        elif q == ')':
            while op[-1] != '(':
                nums.append(op.pop())
            op.pop()

    while op:
        nums.append(op.pop())

    ans = []
    for q in nums:
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

    ans1 = ans.pop()
    print(f'#{p+1} {ans1}')
