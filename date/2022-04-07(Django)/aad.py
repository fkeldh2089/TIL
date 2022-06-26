from collections import deque



num = deque([0])
while 1:
    num[-1] += 1
    for q in range(len(num) - 1, -1, -1):
        if num[q] >= 5:
            num[q] = 0
            if q > 0:
                num[q - 1] += 1
            else:
                num.appendleft(1)
    print(num)
