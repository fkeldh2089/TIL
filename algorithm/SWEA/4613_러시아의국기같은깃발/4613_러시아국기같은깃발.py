# 4613 러시아 국기 같은 깃발
import sys
sys.stdin = open('input_4613.txt')

TC = int(input())

for p in range(TC):
    # N 행, M 열
    N, M = list(map(int, input().split()))
    flag_R = []
    for q in range(N):
        col = input()
        cnt_W, cnt_B, cnt_R = 0, 0, 0
        for q1 in range(M):
            if col[q1] == 'W':
                cnt_W += 1
            if col[q1] == 'B':
                cnt_B += 1
            if col[q1] == 'R':
                cnt_R += 1
        flag_R.append([cnt_W, cnt_B, cnt_R])  # 갯수들로 변환
    flag_R2 = flag_R[1:-1]  # 어차피 내용안바꿈, 얕은 복사

    # 맨윗줄, 아랫줄 카운트
    de_cnt = flag_R[0][1] + flag_R[0][2] + flag_R[-1][0] + flag_R[-1][1]

    # 맨 위는 W, 맨 아래는 R로 채우는 건 확실, 나머지가 문제
    # 몇줄 몇줄 만들 것인지부터 생각해봅시다.
    ans = 0
    f = 0
    for q1 in range(1, N-1):  # q1은 파란줄 갯수
        for q2 in range(N-q1-1):  # q2는 하얀줄 갯수, 빨간줄 갯수는 정해짐
            cnt = 0
            for r in range(q2):  # 하얀줄부터 계산
                cnt += flag_R2[r][1]  # 파랑 -> 하양
                cnt += flag_R2[r][2]  # 빨강 -> 하양

            for r in range(q1):  # 파랑줄 계산
                cnt += flag_R2[q2 + r][2]  # 빨강 -> 파랑
                cnt += flag_R2[q2 + r][0]  # 하양 -> 파랑

            for r in range(N-q1-q2-2):  # 빨강줄 계산
                cnt += flag_R2[q1 + q2 + r][0]  # 하양 -> 빨강
                cnt += flag_R2[q1 + q2 + r][1]  # 파랑 -> 빨강

            if f == 0:
                ans = cnt
                f = 1
            elif f == 1:
                if ans > cnt:
                    ans = cnt

    print(f'#{p+1} {ans + de_cnt}')