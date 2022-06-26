# 1945 간단한 소인수 분해
import sys
sys.stdin = open('input_1945.txt')

tc = int(input())

for p in range(tc):
    num = int(input())
    compo = [0] *5

    while(num !=  1): # 각각 숫자로 나눠지면 카운트 하면서 쪼개기
        if num % 2 == 0:
            num = num // 2
            compo[0] += 1
        if num % 3 == 0:
            num = num // 3
            compo[1] += 1
        if num % 5 == 0:
            num = num // 5
            compo[2] += 1
        if num % 7 == 0:
            num = num // 7
            compo[3] += 1
        if num % 11 == 0:
            num = num // 11
            compo[4] += 1

    ans = ' '.join(map(str, compo))
    print(f'#{p+1} {ans}')
