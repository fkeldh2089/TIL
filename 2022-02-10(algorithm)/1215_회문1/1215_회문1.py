# 1215 회문1
import sys
sys.stdin = open('input_1215.txt')


def make_word(n, mt):
    words = []
    for q in range(8 - n + 1):
        for p in range(8):
            tmp2 = ''
            for p1 in range(n):
                tmp2 += mt[q + p1][p]
            words.append(tmp2)

    for q in range(8 - n + 1):
        for p in range(8):
            tmp1 = ''
            for p1 in range(n):
                tmp1 += mt[p][q + p1]
            words.append(tmp1)
    return words


def confirm_r(m):
    if m == m[::-1]:
        return 0
    else:
        return -1


for p in range(10):
    N = int(input())
    mat = []

    for q in range(8):
        col = input()
        mat.append(col)

    new_words = make_word(N, mat)
    cnt = 0
    for q in range(len(new_words)):
        if confirm_r(new_words[q]) == 0:
            cnt += 1

    print(f'#{p+1} {cnt}')

