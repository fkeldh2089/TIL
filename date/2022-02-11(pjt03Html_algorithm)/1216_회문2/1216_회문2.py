# 1216 회문
import sys
sys.stdin = open('input_1216.txt')

# 1 완전 탐색
def make_word(n, mt):
    words = []
    for q in range(100 - n + 1):
        for p in range(100):
            tmp2 = ''
            for p1 in range(n):
                tmp2 += mt[q + p1][p]
            words.append(tmp2)

    for q in range(100 - n + 1):
        for p in range(100):
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
    for q in range(100):
        col = input()
        mat.append(col)

    #print(mat)
    for q in range(100):
        new_words = make_word(100 - q, mat)
        #print(new_words)
        cnt = 0
        for q1 in range(len(new_words)):
            if confirm_r(new_words[q1]) == 0:
                cnt += 1
        if cnt > 0:
            ans = 100 - q
            break

    print(f'#{N} {ans}')