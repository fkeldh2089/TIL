# 2578 빙고
import sys
sys.stdin = open('input_2578.txt')


def conf(n, m):  # 주어진 숫자 n이 보드 m 어디위에 있는가
    a, b = 0, 0
    for p1 in range(5):
        for p2 in range(5):
            if m[p1][p2] == n:
                a = p1
                b = p2
    return [a, b]


board = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]

cnt_r = [0] * 5  # 행 개수
cnt_c = [0] * 5  # 열 개수
cnt1 = 0  # 정방향 대각선 카운트
cnt2 = 0  # 역방향 대각선 카운트
f = 0
for p in range(25):
    #print(nums[p//5][p%5])
    pos = conf(nums[p//5][p % 5], board)
    cnt_r[pos[0]] += 1
    cnt_c[pos[1]] += 1

    if pos[0] == 2 and pos[1] == 2:
        cnt1 += 1
        cnt2 += 1
    else:
        if pos[0] == pos[1]:
            cnt1 += 1
        if pos[0] + pos[1] == 4:
            cnt2 += 1

    for q in range(5):
        if cnt_r[q] == 5:
            f += 1
            cnt_r[q] = 0
        if cnt_c[q] == 5:
            f += 1
            cnt_c[q] = 0
    if cnt1 == 5:
        f += 1
        cnt1 = 0
    if cnt2 == 5:
        f += 1
        cnt2 = 0

    if f >= 3:
        ans = p + 1
        break

print(ans)