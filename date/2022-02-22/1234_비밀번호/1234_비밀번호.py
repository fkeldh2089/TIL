# 1234 비밀번호
import sys
sys.stdin = open('input_1234.txt')

for p in range(10):
    l, sen = input().split()
    stack = []
    top = -1
    for q in sen:
        stack.append(q)
        top += 1
        if top >= 1 and stack[top] == stack[top - 1]:
            stack.pop()
            stack.pop()
            top -= 2
    ans = int(''.join(stack))
    print(f'#{p+1} {ans}')