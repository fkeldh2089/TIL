# 5356 의석이의 세로로 말해요
import sys
sys.stdin = open('input_5356.txt')

TC = int(input())
for p in range(TC):
    board = [[0]*15 for _ in range(5)]  # 칠판
    for q in range(5):
        word = input()
        board[q][0:len(word)] = word

    ans = ''
    for q1 in range(15):
        for q2 in range(5):
            if board[q2][q1] != 0:
                ans += board[q2][q1]
    print(f'#{p+1} {ans}')
