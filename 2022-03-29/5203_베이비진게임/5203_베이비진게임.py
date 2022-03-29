# 5203 컨테이너 운반
import sys
sys.stdin = open('input_5203.txt')


TC = int(input())
for p in range(TC):
    cards = list(map(int, input().split()))
    cnt1 = [0]*10
    cnt2 = [0]*10
    f = 1
    a = 0

    while a == 0 and cards:
        tmp = cards.pop(0)
        if f == 1:
            cnt1[tmp] += 1
            f = 2
            for q in range(10):
                if cnt1[q] >= 3:
                    a = 1
            for q in range(8):
                for q1 in range(3):
                    if cnt1[q+q1] < 1:
                        break
                else:
                    a = 1

        elif f == 2:
            cnt2[tmp] += 1
            f = 1
            for q in range(10):
                if cnt2[q] >= 3:
                    a = 2
            for q in range(8):
                for q1 in range(3):
                    if cnt2[q+q1] < 1:
                        break
                else:
                    a = 2
    print(f'#{p+1} {a}')
