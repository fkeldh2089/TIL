# 4873 반복문자 지우기
import sys
sys.stdin = open('input_4873.txt')

TC = int(input())

for p in range(TC):
    sen = input()
    stack = []
    top = -1
    for q in sen:
        stack.append(q)
        top += 1
        if top >= 1 and stack[top] == stack[top - 1]:
            stack.pop()
            stack.pop()
            top -= 2
    print(f'#{p+1} {top + 1}')
