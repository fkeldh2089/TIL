# 연습문제 3
import sys
sys.stdin = open('input_ex3.txt')
from collections import deque


nums = [
    '001101', '010011', '111011', '110001',
    '100011', '110111', '001011', '111101',
    '011001', '101111'
]

TC = int(input())
for p in range(TC):
    N = input()
    cnt = 0
    ans = deque()
    for q in range(len(N)):
        if N[q] == '0':
            cnt += 1
        else:
            break
    N = int(N, 16)
    N = bin(N)
    N = N.replace('0b', '')
    if len(N) % 4:
        N = '0'*(4 - len(N) % 4) + N
    N = '0'*(cnt*4) + N
    word = N
    word = word.rstrip('0')
    l = len(word) // 6
    for q in range(l):
        for q1 in range(10):
            if word[-6:] == nums[q1]:
                ans.appendleft(q1)
                word = word[:-6]
                break
        else:
            break
    print(f'#{p + 1} {" ".join(list(map(str, ans)))}')