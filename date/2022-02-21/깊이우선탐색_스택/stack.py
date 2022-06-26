# stack
# import sys
# sys.stdin = open('input_stack')


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
        return stack[top+1]


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


size = 10
stack = [0] * size
top = -1

push(10, size)
print(stack)
push(30, size)
print(stack)
push(20, size)
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)
print(pop())
print(stack)
push(20, size)
print(stack)
print(pop())