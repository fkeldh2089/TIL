# 4866 괄호검사
import sys
sys.stdin = open('input_4866.txt')

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return
    else:
        return stack.pop()

def is_empty():
    if len(stack) == 0:
        return True
    else:
        return False

def check_matching(data):
    for i in range(len(data)):
        if data[i] == '(':
            push(data[i])
        elif data[i] == '{':
            push(data[i])
        elif data[i] == ')':
            if is_empty():
                return 0
            if stack[-1] == '(':
                pop()
            else:
                return 0
        elif data[i] == '}':
            if is_empty():
                return 0
            if stack[-1] == '{':
                pop()
            else:
                return 0
    if not is_empty():
        return 0
    else:
        return 1

TC_num = int(input())

for i in range(TC_num):
    stack = []
    data = input()

    print(f'#{i+1} {check_matching(data)}')