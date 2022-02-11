# 1221 GNS
import sys
sys.stdin = open('input_1221.txt')


def trans(n):  # 지구어로 변환
    if n == 'ZRO':
        return 0
    elif n == 'ONE':
        return 1
    elif n == 'TWO':
        return 2
    elif n == 'THR':
        return 3
    elif n == 'FOR':
        return 4
    elif n == 'FIV':
        return 5
    elif n == 'SIX':
        return 6
    elif n == 'SVN':
        return 7
    elif n == 'EGT':
        return 8
    elif n == 'NIN':
        return 9


def utrans(n):  # 역변환
    if n == 0:
        return 'ZRO'
    elif n == 1:
        return 'ONE'
    elif n == 2:
        return 'TWO'
    elif n == 3:
        return 'THR'
    elif n == 4:
        return 'FOR'
    elif n == 5:
        return 'FIV'
    elif n == 6:
        return 'SIX'
    elif n == 7:
        return 'SVN'
    elif n == 8:
        return 'EGT'
    elif n == 9:
        return 'NIN'


def sort(n, m):  # 소트
    for p in range(n-1):
        for p1 in range(n-1):
            if m[p1] > m[p1+1]:
                m[p1], m[p1+1] = m[p1+1], m[p1]
    return m


TC = int(input())
for p in range(TC):
    TR, OP = input().split()
    num = int(OP)
    SN = input().split()
    EN = []
    RSN = []

    for q in range(num):
        EN.append(trans(SN[q]))
    #print(EN)
    m = sort(num, EN)
    #print(m)
    for q in range(num):
        RSN.append(utrans(m[q]))
    #print(RSN)
    print(f'#{p+1}')
    print(' '.join(RSN))

