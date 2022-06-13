from collections import deque, defaultdict
from itertools import permutations


def minmove(r, c, tr, tc, board):
    print(f'start: {r, c}')
    if r == tr and c == tc:
        return 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    stack = deque()
    visited = [[1] * 4 for _ in range(4)]
    stack.append([r, c, 0])
    visited[r][c] = 0
    while stack:
        r, c, cnt = stack.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                cr, cc = r, c
                while 1:
                    cr += dr[d]
                    cc += dc[d]
                    if 0 <= cr < 4 and 0 <= cc < 4:
                        if board[cr][cc]:
                            break
                    else:
                        cr -= dr[d]
                        cc -= dc[d]
                        break
                if (nr == tr and nc == tc) or (cr == tr and cc == tc):
                    print(f'end: {nr, nc} or {cr, cc}, {cnt}')
                    return cnt + 1
                if visited[nr][nc]:
                    stack.append([nr, nc, cnt + 1])
                    visited[nr][nc] = 0
                if visited[cr][cc]:
                    stack.append([cr, cc, cnt + 1])
                    visited[cr][cc] = 0


def mingame(cardOrder, r, c, idx, cnt, board, cards):
    global M
    print(f'r, c: {r, c}')
    print(idx, cnt)
    if idx == len(cardOrder)-1:
        if M > cnt:
            M = cnt
        return
    cnt1 = cnt + minmove(r, c, cards[cardOrder[idx + 1]][0][0], cards[cardOrder[idx + 1]][0][1], board) + minmove(
        cards[cardOrder[idx + 1]][0][0], cards[cardOrder[idx + 1]][0][1], cards[cardOrder[idx + 1]][1][0],
        cards[cardOrder[idx + 1]][1][1], board) + 2
    cnt2 = cnt + minmove(r, c, cards[cardOrder[idx + 1]][1][0], cards[cardOrder[idx + 1]][1][1], board) + minmove(
        cards[cardOrder[idx + 1]][1][0], cards[cardOrder[idx + 1]][1][1], cards[cardOrder[idx + 1]][0][0],
        cards[cardOrder[idx + 1]][0][1], board) + 2
    board1 = [row[:] for row in board]
    board1[cards[cardOrder[idx + 1]][0][0]][cards[cardOrder[idx + 1]][0][1]] = 0
    board1[cards[cardOrder[idx + 1]][1][0]][cards[cardOrder[idx + 1]][1][1]] = 0
    mingame(cardOrder, cards[cardOrder[idx + 1]][1][0], cards[cardOrder[idx + 1]][1][1], idx + 1, cnt1, board1, cards)
    mingame(cardOrder, cards[cardOrder[idx + 1]][0][0], cards[cardOrder[idx + 1]][0][1], idx + 1, cnt2, board1, cards)


M = 16 ** 6


def solution(board, r, c):
    # 16개면 brutal
    global M
    answer = 0
    cards = defaultdict(list)
    cardnum = []
    for q1 in range(4):
        for q2 in range(4):
            if board[q1][q2]:
                cards[board[q1][q2]].append([q1, q2])
                if board[q1][q2] not in cardnum:
                    cardnum.append(board[q1][q2])
    print(cards)
    # 1. 카드 처리 순서
    for p in permutations(cardnum, len(cardnum)):
        print(p)
        mingame(p, r, c, -1, 0, board, cards)

    answer = M
    # 2. 이동 최소 거리 구하기
    return answer


board = [[0,0,0,4],[0,0,0,0],[0,0,0,0],[4,0,0,0]]
r, c = 1, 0

print(solution(board, r, c))