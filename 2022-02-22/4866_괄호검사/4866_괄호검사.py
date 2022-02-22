# 4866 괄호검사
import sys
sys.stdin = open('input_4866.txt')


class Stack:
    def __init__(self, size):
        self.size = size
        self.items = [None] * self.size
        self.top = -1

    def is_empty(self):
        return True if (self.top == -1) else False

    def is_full(self):
        return True if (self.top == self.size) else False

    def push(self, item):
        if self.is_full():
            raise Exception('FUll')
        else:
            self.top += 1
            self.items[self.top] = item

    def peek(self):
        if self.is_empty():
            raise Exception('emp')
        else:
            return self.items[self.top]

    def pop(self):
        if self.is_empty():
            raise Exception('emp')
        else:
            value = self.items[self.top]
            self.items[self.top] = None
            self.top -= 1
            return value

    def __str__(self):
        result = '\n-----'
        for item in self.items:
            if item is None:
                result = f'\n|      |' + result
            else:
                result = f'\n|  {item}  |' + result
        return result


TC = int(input())

# for p in range(TC):
#     stack = []
#     top = -1
#     dia = input()
#     for q in dia:
#         if q == '(':
#             stack.append(q)
#             top += 1
#         elif q == ')':
#             top -= 1
#             if top < -1:
#                 a = 0
#                 break
#             if stack.pop() != '(':
#                 a = 0
#                 break
#         if q == '{':
#             stack.append(q)
#             top += 1
#
#         elif q == '}':
#             top -= 1
#             if top < -1:
#                 a = 0
#                 break
#             if stack.pop() != '{':
#                 a = 0
#                 break
#     else:
#         if top == -1:
#             a = 1
#         else:
#             a = 0
#     print(f'#{p+1} {a}')

for p in range(TC):
    sen = input()
    n = len(sen)
    dia = Stack(n)
    for q in sen:
        if q == '(':
            dia.push(q)
        elif q == ')':
            if dia.top == -1:
                a = 0
                break
            if dia.pop() != '(':
                a = 0
                break
        if q == '{':
            dia.push(q)

        elif q == '}':
            if dia.top == -1:
                a = 0
                break
            if dia.pop() != '{':
                a = 0
                break
    else:
        if dia.is_empty():
            a = 1
        else:
            a = 0
    print(f'#{p+1} {a}')
