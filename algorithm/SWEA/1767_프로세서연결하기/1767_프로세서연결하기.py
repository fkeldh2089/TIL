# 1767 프로세서 연결하기
import sys
from pprint import pprint
sys.stdin = open('input_1767.txt')

from copy import deepcopy


def line(i, d):  # 선 연결
    r, c, k = core[i]
    global cnt, cnt2, cnt3
    if d == 0:  # 해당 코어의 위쪽
        for q1 in range(r):
            if tmp_field[q1][c] != 0:
                cnt2 += 1
                break
        else:  # 해당 코어 위가 모두 비어 있다면,
            for q2 in range(r):
                tmp_field[q2][c] = 2  # 세로 선 연결
                cnt3 += 1
            cnt += 1

    elif d == 1:  # 해당 코어의 아래쪽
        for q1 in range(r + 1, N):
            if tmp_field[q1][c] != 0:
                cnt2 += 1
                break
        else:  # 해당 코어 아래가 모두 비어 있다면,
            for q2 in range(r + 1, N):
                tmp_field[q2][c] = 2  # 세로 선 연결
                cnt3 += 1
            cnt += 1

    elif d == 3:  # 해당 코어의 오른쪽
        for q1 in range(c + 1, N):
            if tmp_field[r][q1] != 0:
                cnt2 += 1
                break
        else:  # 해당 코어 오른쪽이 모두 비어 있다면,
            for q2 in range(c + 1, N):
                tmp_field[r][q2] = 3  # 가로 선 연결
                cnt3 += 1
            cnt += 1

    elif d == 2:  # 해당 코어의 왼쪽
        for q1 in range(c):
            if tmp_field[r][q1] != 0:
                cnt2 += 1
                break
        else:  # 해당 코어 왼쪽이 모두 비어 있다면,
            for q2 in range(c):
                tmp_field[r][q2] = 3  # 가로 선 연결
                cnt3 += 1
            cnt += 1
    elif d == 5:
        pass


def con(q1, q2):
    tmp_d = []
    for s1 in range(q1):
        if tmp_field[s1][q2] != 0:
            break
    else:
        tmp_d.append(0)
    for s1 in range(q1 + 1, N):
        if tmp_field[s1][q2] != 0:
            break
    else:  # 해당 코어 아래가 모두 비어 있다면,
        tmp_d.append(1)
    for s1 in range(q2):  # 왼쪽이 비어있으면,,
        if tmp_field[q1][s1] != 0:
            break
    else:
        tmp_d.append(2)
    for s1 in range(q2 + 1, N):  # 오른쪽이 비어있으면,,
        if tmp_field[q1][s1] != 0:
            break
    else:
        tmp_d.append(3)
    return tmp_d


TC = int(input())

for p in range(TC):
    N = int(input())  # 필드 크기
    field = [list(map(int, input().split())) for _ in range(N)]
    core = []
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    mn = 0
    mn_line = 0
    ans = []
    numbers = []
    tmp_cnt = 0

    for q1 in range(N):
        for q2 in range(N):
            tmp_d = []
            if field[q1][q2] == 1 and q1 != 0 and q2 != 0 and q1 != N-1 and q2 != N-1:  # 벽에 안붙은 코어
                cnt5 = 0
                for s1 in range(q1):
                    cnt5 += 1
                    if field[s1][q2] != 0:
                        break
                else:  # 해당 코어 위쪽이 비어있으면,
                    if cnt5 == 1:
                        tmp_cnt += 1
                        continue
                    tmp_d.append([0, cnt5])
                cnt5 = 0
                for s1 in range(q1 + 1, N):
                    cnt5 += 1
                    if field[s1][q2] != 0:
                        break
                else:  # 해당 코어 아래가 모두 비어 있다면,
                    if cnt5 == 1:
                        tmp_cnt += 1
                        continue
                    tmp_d.append([1, cnt5])
                cnt5 = 0
                for s1 in range(q2):
                    cnt5 += 1
                    if field[q1][s1] != 0:
                        break
                else:  # 왼쪽이 비어있으면,,
                    if cnt5 == 1:
                        tmp_cnt += 1
                        continue
                    tmp_d.append([2, cnt5])
                cnt5 = 0
                for s1 in range(q2 + 1, N):
                    cnt5 += 1
                    if field[q1][s1] != 0:
                        break
                else:  # 오른쪽이 비어있으면,,
                    if cnt5 == 1:
                        tmp_cnt += 1
                        continue
                    tmp_d.append([3, cnt5])

                tmp_d.append([5, 0])
                if tmp_d != [5]:
                    core.append([q1, q2, tmp_d])  # 코어 탐색
                    numbers.append(len(tmp_d))
    # print(core)
    k = len(core)
    core_list = [0] * k
    i = k-1
    f = 0

    while k > 0:
        tmp_field = deepcopy(field)
        cnt = 0
        cnt2 = 0
        cnt3 = 0
        for q3 in range(k):
            line(q3, core[q3][2][core_list[q3]][0])
            if cnt2 > (k - mn):
                break
            if mn == k and cnt3 > mn_line:
                break

        if mn <= cnt:
            if mn < cnt:
                mn = cnt
                mn_line = cnt3
                # if cnt1 == 26 and cnt == 9:
                #     print(core_list, cnt, ans)
                #     pprint(tmp_field)
            else:
                if cnt3 < mn_line:
                    mn_line = cnt3

                # if cnt1 == 26 and cnt == 9:
                #     print(core_list, cnt, ans)
                #     pprint(tmp_field)

        if numbers[i]-1 > core_list[i]:
            core_list[i] += 1
        else:
            while numbers[i]-1 <= core_list[i]:
                core_list[i] = 0
                i -= 1
            if i == -1:
                break
            core_list[i] += 1
            i = k-1
    print(f'#{p+1} {mn_line+tmp_cnt}')




    # num = 4**k
    # for q1 in range(num):
    #     result1 = numeral_system(q1, 4)
    #     core_list = [0] * k
    #     for q2 in range(k-len(result1), k):
    #         core_list[q2] = int(result1[len(result1)-(k-q2)])
    #         tmp_field = deepcopy(field)  # 임시 필드
    #         cnt = 0
    #     for q3 in range(k):
    #         line(q3, core_list[q3])
    #     if mn <= cnt:
    #         cnt1 = 0
    #         for s1 in range(N):
    #             for s2 in range(N):
    #                 if tmp_field[s1][s2] == 2 or tmp_field[s1][s2] == 3:
    #                     cnt1 += 1
    #         if mn < cnt:
    #             mn = cnt
    #             ans = [cnt1]
    #             # print(core_list, cnt, ans)
    #             # pprint(tmp_field)
    #         else:
    #             ans.append(cnt1)
    #             # print(core_list, cnt, ans)
    #             # pprint(tmp_field)
    #
    # print(f'#{p+1} {min(ans)}')
