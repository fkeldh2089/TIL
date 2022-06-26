# stack

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
        return  result

a = Stack(5)
print(a)
a.push(10)
print(a)
a.push(25)
print(a)
a.push(32)
print(a)
a.pop()
print(a)
a.pop()
print(a)
a.pop()
print(a)