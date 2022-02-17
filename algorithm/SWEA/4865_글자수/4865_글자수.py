# 4865 글자수
import sys
sys.stdin = open('input_4865.txt')

TC = int(input())

for p in range(TC):
    OB = input()
    ST = input()

    OB_l = len(OB)
    ST_l = len(ST)

    ans = 0
    for q1 in OB:
        cnt = 0
        for q2 in ST:
            if q1 == q2:
                cnt += 1
            if cnt > ans:
                ans = cnt

    print(f'#{p+1} {ans}')

    # i = 0  # 큰 문자열의 index
    # ans = 0  # 반복된 횟수
    # cnt = 1  # 작은 문자열의 index
    # while i < ST_l - OB_l - 1:
    #     if OB[cnt-1] == ST[i+cnt-1]:
    #         cnt += 1
    #     else:
    #         i += cnt
    #         cnt = 1
    #
    #     if cnt == OB_l + 1:
    #         ans += 1
    #         i += cnt
    #         cnt = 1

    #print(ans)



