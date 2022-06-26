# 4880 토너먼트 카드 게임
import sys
sys.stdin = open('input_4880.txt')


def game(mat):
    if len(mat) == 2:
        if mat[0][1] == 1:
            if mat[1][1] == 3 or mat[1][1] == 1:
                return mat[0]
            else:
                return mat[1]
        elif mat[0][1] == 2:
            if mat[1][1] == 1 or mat[1][1] == 2:
                return mat[0]
            else:
                return mat[1]
        elif mat[0][1] == 3:
            if mat[1][1] == 2 or mat[1][1] == 3:
                return mat[0]
            else:
                return mat[1]
    elif len(mat) == 1:
        return mat[0]


def group(mat):
    global ta
    s = 1
    e = len(mat)
    idx = (s + e)//2
    if len(mat) == 1 or len(mat) == 2:
        ta.append(mat)
    else:
        group(mat[0:idx])
        group(mat[idx:])


TC = int(input())

for p in range(TC):
    N = int(input())
    card = list(map(int, input().split()))
    mat = []
    ta = []  # 그룹들

    for q in range(N):
        mat.append([q+1, card[q]])

    while len(mat) > 1:
        group((mat))  # 그룹으로 묶고
        mat = []  # mat 초기화
        for q in range(len(ta)):
            tmp = game(ta[q])  # 각 그룹의 승자
            mat.append(tmp)  # mat에 넣어주고
        ta = []

    ans = mat[0][0]
    print(f'#{p+1} {ans}')