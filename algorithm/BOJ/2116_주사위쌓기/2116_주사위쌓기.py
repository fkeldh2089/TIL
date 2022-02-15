import sys
sys.stdin = open('input_2116.txt')


def dice_oppo(n):  # 주사위 반대편 숫자 출력
    if n == 0:
        return 5
    elif n == 1:
        return 3
    elif n == 2:
        return 4
    elif n == 3:
        return 1
    elif n == 4:
        return 2
    else:
        return 0


N = int(input())

# 어차피 아래 하나가 정해지면 끝까지 간다.
dices = []
for p in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)  # 다이스들

max_num = 0
for p in range(6):  # 맨 아래 하나의 주사위 6가지 경우에 대하여
    p_o = dice_oppo(p)  # 맨 아랫면의 반대편
    dice_l = dices[0][p]  # 아랫면 숫자
    de_sum = 6 * N  # 기본값을 최대값으로 정하고,,

    for p1 in range(N):  # 주사위 갯수만큼 반복
        dice_h = dices[p1][p_o]  # 윗면 숫자
        if dice_l == 6 or dice_h == 6:  # 맨 위나 아래에 6이 있으면,,
            de_sum -= 1  # 1 빼주고
            if dice_l == 5 or dice_h == 5:  # 6도 있고 5도 있으면,,
                de_sum -= 1  # 1 더 빼준다.

        for p2 in range(6):  # 다음 주사위 아랫면 찾기
            if p1 + 1 == N:
                break
            if dice_h == dices[p1 + 1][p2]:  # 아래 주사위와 위의 아랫면
                p_o = dice_oppo(p2)  # 반대편 찾음
                dice_l = dice_h
                break

    # print(f'#{p} de_sum : {de_sum}')
    if max_num <= de_sum:
        max_num = de_sum

print(max_num)