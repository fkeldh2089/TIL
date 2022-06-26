# 1242 암호코드 스캔
import sys
sys.stdin = open('input_1242.txt')
from collections import deque
nums = [
    '0001101', '0011001', '0010011', '0111101',
    '0100011', '0110001', '0101111', '0111011',
    '0110111', '0001011'
]
TC = int(input())
for p in range(TC):
    N, M = map(int, input().strip().split())
    mat = [input().rstrip('0') for _ in range(N)]
    # print(mat)
    ans = deque()
    mn = 0
    mat2 = []
    print(mat)
    for q in range(N):
        if mat[q] != '':
            for q1 in range(len(mat[q])):
                if mat[q][q1] == '0':
                    mat2 += mat[q].split('0')
                    break
            else:
                mat2.append(mat[q])

    print(mat2)
    for q in range(N):
        if mn < len(mat[q]):
            words = mat[q].split('0')
            mn = len(mat[q])
    # print(words)
    sub_sum = 0
    for r in range(len(words)):
        word = words[r]
        word = bin(int(word, 16)).replace('0b','000000')
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
        sub_sum += sub
    print(f'#{p+1} {sub_sum}')
