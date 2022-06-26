# 1223 계산기 1
import sys
sys.stdin = open('input_1222.txt')

for p in range(10):
    N = int(input())
    cal = input()
    ans = []
    for q in cal:
        if q != '+':
            ans.append(int(q))

    ans1 = 0
    for q in ans:
        ans1 += q

    print(f'#{p+1} {ans1}')
