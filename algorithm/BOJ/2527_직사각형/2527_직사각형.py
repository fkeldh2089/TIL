# 2527 직사각형
import sys
sys.stdin = open('input_2527.txt')

# 하나씩 처리하자
for p in range(4):
    points = list(map(int, input().split()))
    rec1 = points[0:4]
    rec2 = points[4:8]
    # 샘플링하는 기분으로 갑시다 rec1* rec2 - 시간 초과,,
    # 머리를 씁시다. 기준 직사각형을 중심으로 8 영역으로 쪼개자 (차선)
    cnt1 = 0  # 카운트
    cnt2 = 0
    tmp = -5
    for q in range(rec1[1], rec1[3] + 1):
        if rec2[1] <= q <= (rec2[3]):
            cnt1 += 1
    for q1 in range(rec1[0], rec1[2] + 1):
        if rec2[0] <= q1 <= (rec2[2]):
            cnt2 += 1

    if cnt1 == 0 or cnt2 == 0:
        print('d')
    elif cnt1 == 1 and cnt2 == 1:
        print('c')
    elif cnt1 == 1 or cnt2 == 1:
        print('b')
    else:
        print('a')




