# 연습문제 1
import sys
sys.stdin = open('input_ex1.txt')

TC = int(input())

for p in range(TC):
    N = input()
    ans = []
    for q1 in range(len(N)//7):
        cnt = 0
        for q in range(7):
            if N[-1-(q)+7*(q1+1)] == '1':
                cnt += 2**q
        ans.append(cnt)
    if len(N)%7:
        for q1 in range(len(N)%7):
            cnt = 0
            if N[-1-q1] == '1':
                cnt += 2**q1
        ans.append(cnt)
    print(f'#{p+1} {ans}')
