# 1979 어디에 단어가 들어갈까
import sys
sys.stdin = open('input_1979.txt')

TC = int(input())

for p in range(TC):
    N, K = list(map(int, input().split()))
    numbs = []
    for q in range(N):
        col = list(map(int, input().split()))
        numbs.append(col)
    f_x = 0  # 플래그
    f_y = 0

    cnt_x = 0
    cnt_y = 0
    ans = 0
    for q1 in range(N):
        for q2 in range(N):
            if numbs[q1][q2] == 1:  # 1이면 카운트
                f_x = 1
                cnt_x += 1
            else:  # 0 만나면 카운트갯수가 원하는 숫자일 경우,,,
                if f_x == 1:
                    if cnt_x == K:
                        ans += 1
                        cnt_x = 0
                    else:
                        cnt_x = 0

            if numbs[q2][q1] == 1:
                f_y = 1
                cnt_y += 1
            else:
                if f_y == 1:
                    if cnt_y == K:
                        ans += 1
                        cnt_y = 0
                    else:
                        cnt_y = 0
            if q2 == (N-1):  # 마지막 줄은 별도 처리
                if cnt_y == K:
                    ans += 1
                    cnt_y = 0
                else:
                    cnt_y = 0

                if cnt_x == K:
                    ans += 1
                    cnt_x = 0
                else:
                    cnt_x = 0

    print(f'#{p+1} {ans}')

