from pprint import pprint

board = [[0,7,0,0,0,0,0,0,0,0],[7,7,7,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]

block_dic = {'122': 1, '133': 2, '113': 3, '112': 4, '124': 5}
dr = [-1, 1, 0, 0, 0]
dc = [0, 0, -1, 1, 2]
N = len(board)
twice = [[0]*N for _ in range(N)]
cnt = 0
cnt2 = 0
for q1 in range(N):
    for q2 in range(N):
        if board[q1][q2] != 0 and twice[q1][q2] == 0:
            r, c = q1, q2
            twice[q1][q2] = 1
            tmp_piece = ''
            while 1:
                for d in range(5):
                    nr, nc = r+dr[d], c+dc[d]
                    if 0<=nr<N and 0<=nc<N and board[nr][nc]==board[q1][q2] and twice[nr][nc]==0:
                        tmp_piece += str(d)
                        twice[nr][nc] = 1
                        r, c = nr, nc
                        break
                else:
                    break
            if block_dic.get(tmp_piece):

                if block_dic.get(tmp_piece) == 1:
                    for qq in range(0, q1+1):
                        if board[qq][q2-1] + board[qq][q2-2] != 0:
                            break
                    else:
                        board[q1][q2] = 0
                        board[q1+1][q2] = 0
                        board[q1+1][q2-1] = 0
                        board[q1+1][q2-2] = 0
                        cnt += 1

                elif block_dic.get(tmp_piece) == 2:
                    for qq in range(0, q1+1):
                        if board[qq][q2+2] + board[qq][q2+1] != 0:
                            break
                    else:
                        board[q1][q2] = 0
                        board[q1+1][q2] = 0
                        board[q1+1][q2+2] = 0
                        board[q1+1][q2+1] = 0
                        cnt += 1

                elif block_dic.get(tmp_piece) == 3:
                    for qq in range(0, q1+2):
                        if board[qq][q2+1] != 0:
                            break
                    else:
                        board[q1][q2] = 0
                        board[q1+1][q2] = 0
                        board[q1+2][q2] = 0
                        board[q1+2][q2+1] = 0
                        cnt += 1
                elif block_dic.get(tmp_piece) == 4:
                    for qq in range(0, q1+2):
                        if board[qq][q2-1] != 0:
                            break
                    else:
                        board[q1][q2] = 0
                        board[q1+1][q2] = 0
                        board[q1+2][q2] = 0
                        board[q1+2][q2-1] = 0
                        cnt += 1
                elif block_dic.get(tmp_piece) == 5:
                    for qq in range(0, q1+1):
                        if board[qq][q2-1] + board[qq][q2+1] != 0:
                            break
                    else:
                        board[q1][q2] = 0
                        board[q1+1][q2] = 0
                        board[q1+1][q2-1] = 0
                        board[q1+1][q2+1] = 0
                        cnt += 1

pprint(board)
