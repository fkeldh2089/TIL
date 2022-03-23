# 1240 단순 2진 암호 코드
import sys
sys.stdin = open('input_1240.txt')
from collections import deque
nums = [
    '0001101', '0011001', '0010011', '0111101',
    '0100011', '0110001', '0101111', '0111011',
    '0110111', '0001011'
]
TC = int(input())
for p in range(TC):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    ans = deque()
    for q in range(N):
        if mat[q] != '0'*M:
            word = mat[q]
    word = word.rstrip('0')
    l = len(word)//7
    for q in range(l):
        for q1 in range(10):
            if word[-7:] == nums[q1]:
                ans.appendleft(q1)
                word = word[:-7]
                break
        else:
            break

    odd_num = 0
    even_num = 0
    for q in range(4):
        odd_num += ans[2*q]
        even_num += ans[2*q+1]
    answer = 3*odd_num + even_num
    if answer%10:
        sub = 0
    else:
        sub = odd_num + even_num

    print(f'#{p+1} {sub}')
