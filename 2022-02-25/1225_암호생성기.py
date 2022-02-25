# 1225 암호생성기
import sys
from collections import deque
sys.stdin = open('input_1225.txt')

for p in range(1, 11):
    TC = int(input())
    pa = deque(map(int, input().split()))

    while 1:
        for q in range(1, 6):
            tmp = pa.popleft()
            tmp2 = tmp - q
            if tmp2 > 0:
                pa.append(tmp2)
            else:
                tmp2 = 0
                pa.append(tmp2)
                break

        if pa[-1] == 0:
            break

    print(f'#{TC} ', end = '')
    print(*pa)
