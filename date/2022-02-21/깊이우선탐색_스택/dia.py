import sys
sys.stdin = open('input_dia.txt')

def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item


def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]


def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False


def peek():
    global top
    if top == -1:
        print('Empty')
    else:
        return stack[top]


for p in range(2):
    size = 30
    stack = [0] * size
    top = -1
    dia = input()
    for q in dia:
        if q == '(':
            push(q, size)
        else:
            if pop() != '(':
                print('False')
                break
    else:
        if isEmpty():
            print('True')
        else:
            print('False')
