# ex1-1 계산기
import sys
sys.stdin = open('input_ex1_1.txt')

TC = int(input())
pri = {'(': -1, '+': 0, '-': 0, '*': 1, '/': 1, ')': -2}

for p in range(TC):
    eq = input()
    nums = []
    op = []
    for q in eq:
        if q != '+' and q != '*' and q != '/' and q != '-' and q != ')' and q != '(':  # 연산자 아니면 숫자로 변환
            nums.append(int(q))

        else:  # 숫자가 아닌 경우
            if q == '(':
                op.append(q)
            elif q == '*':  # *이 가장 높은 연산자
                if len(op) == 0:
                    op.append(q)
                else:
                    while len(op) > 0 and pri['*'] <= pri[op[-1]]:
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
            elif q == '/':
                if len(op) == 0:
                    op.append(q)
                else:
                    while len(op) > 0 and pri['/'] <= pri[op[-1]]:
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
            elif q == '+':
                if len(op) == 0:
                    op.append(q)
                else:
                    while len(op) > 0 and pri['+'] <= pri[op[-1]]:
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
            elif q == '-':
                if len(op) == 0:
                    op.append(q)
                else:
                    while len(op) > 0 and pri['-'] <= pri[op[-1]]:
                        tmp_op = op.pop()
                        nums.append(tmp_op)
                    op.append(q)
            elif q == ')':
                while op[-1] != '(':
                    nums.append(op.pop())
                op.pop()
    while op:
        nums.append(op.pop())

    ans = ''.join(list(map(str, nums)))
    print(f'#{p+1} {ans}')
