# 1974 스도쿠 검증
import sys
sys.stdin = open('input_1974.txt')

TC = int(input())

for p in range(TC):
    Sdoku = []
    for q in range(9):
        col = list(map(int, input().split()))
        Sdoku.append(col)


    ans = 1
    for q in range(9):
        cnt = [0] * 9
        for q1 in range(9):
            if Sdoku[q][q1] != 0: # 가로줄 숫자가 하나씩 나오는지 카운트
                cnt[Sdoku[q][q1]-1] = 1
        #print(cnt)
        if cnt!= [1] * 9:
            ans = 0
            break

    for q in range(9):
        cnt = [0] * 9
        for q1 in range(9):
            if Sdoku[q1][q] != 0:  # 세호줄 숫자가 하나씩 나오는지 카운트
                cnt[Sdoku[q1][q]-1] = 1
        #print(cnt)
        if cnt != [1] * 9:
            ans = 0
            break

    for r1 in range(3):
        for r2 in range(3):
            cnt = [0] * 9
            for q1 in range(3):
                for q2 in range(3):
                    if Sdoku[3*r1 + q1][3*r2 + q2] != 0: # 숫자가 하나씩 나오는지 카운트
                        cnt[Sdoku[3*r1 + q1][3*r2 + q2]-1] = 1
            #print(cnt)
            if cnt != [1] * 9:
                ans = 0
                break

    print(f'#{p+1} {ans}')