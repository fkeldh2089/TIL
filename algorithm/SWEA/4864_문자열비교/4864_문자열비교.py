# 4864 문자열 비교
import sys
sys.stdin = open('input_4864.txt')

TC = int(input())

for p in range(TC):
    OB = input()
    ST = input()
    cnt = 0
    for q in range(len(ST)-len(OB) + 1):
        if OB == ST[q:q+len(OB)]:
            cnt = 1

    print(f'#{p+1} {cnt}')