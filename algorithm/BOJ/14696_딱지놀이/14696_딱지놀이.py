# 14696 딱지놀이
import sys
sys.stdin = open('input_14696.txt')

N = int(input())  # 라운드 수

for p in range(N):  # 라운드 안에서
    H1_N, *H1 = list(map(int, input().split()))  # 딱지 모양
    H2_N, *H2 = list(map(int, input().split()))  # 딱지 모양
    card1 = [0] * 4
    card2 = [0] * 4
    for r in range(H1_N):
        card1[H1[r]-1] += 1
    for r in range(H2_N):
        card2[H2[r]-1] += 1

    for q in range(4):
        if card1[-1 -q] > card2[-1 -q]:
            ans = 'A'
            break
        elif card1[-1 -q] < card2[-1 -q]:
            ans = 'B'
            break
    else:
        ans = 'D'

    print(ans)




