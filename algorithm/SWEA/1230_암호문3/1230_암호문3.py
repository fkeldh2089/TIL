# 1230
import sys
sys.stdin = open('input_1230.txt')

for p in range(10):
    N = int(input())
    PW = input().split()
    M = int(input())
    CM = input().split()

    for q in range(len(CM)):
        if CM[q].isalpha():
            tmp = CM[q]
            if tmp == 'I':
                for q1 in range(int(CM[q+2])):
                    PW.insert(int(CM[q+1])+q1, CM[q+q1+3])
            elif tmp == 'D':
                for q1 in range(int(CM[q+2])):
                    PW.pop(int(CM[q+1])+1)
            elif tmp == 'A':
                for q1 in range(int(CM[q+1])):
                    PW.append(CM[q+q1+2])

    PW = ' '.join(PW[0:10])
    print(f'#{p+1} {PW}')