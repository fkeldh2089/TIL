from pprint import pprint

def BFS(board, N):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    r, c = 0, 0
    stack = [[r, c, 0, -1]]  # [r, c, 비용, 세로(0), 가로(1)]
    visited = [[[1500, 1500] for _ in range(N)] for _ in range(N)]
    visited[0][0] = [0, 0]
    while stack:
        r, c, cnt, f = stack.pop()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 0:
                if d < 2:  # 길이 가로인지 세로인지,,
                    tmp_f = 0
                else:
                    tmp_f = 1

                if f == -1:  # 본래 가던 길이 가로인지 세로인지,,
                    cost = 1
                else:
                    if f != tmp_f:  # 커브면,, 6
                        cost = 6
                    else:  # 아니면 1
                        cost = 1
                if visited[nr][nc][tmp_f] > visited[r][c][f] + cost:
                    visited[nr][nc][tmp_f] = visited[r][c][f] + cost
                    stack.append([nr, nc, visited[r][c][f] + cost, tmp_f])

    return visited


def solution(board):
    answer = 0
    N = len(board)
    visited = BFS(board, N)
    answer = min(visited[N-1][N-1])*100
    return answer

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
print(solution(board))