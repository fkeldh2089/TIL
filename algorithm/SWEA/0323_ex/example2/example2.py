# 연습문제 2
import sys
sys.stdin = open('input_ex2.txt')
TC = int(input())
for p in range(TC):
    N = input()
    cnt = 0
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
    ans = []
    for q1 in range(len(N) // 7):
        cnt = 0
        for q in range(7):
            if N[-1 - (q) + 7 * (q1 + 1)] == '1':
                cnt += 2 ** q
        ans.append(cnt)
    if len(N)%7:
        cnt = 0
        for q1 in range(len(N)%7):
            if N[-1-q1] == '1':
                cnt += 2**q1
        ans.append(cnt)
    print(f'#{p + 1} {ans}')