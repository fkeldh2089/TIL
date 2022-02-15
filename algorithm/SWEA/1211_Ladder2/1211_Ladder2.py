import sys

sys.stdin = open('input_1211.txt')

for p in range(10):
    tc = int(input())
    ladder = []
    for q in range(100):
        ladder_c = list(map(int, input().split()))
        ladder.append(ladder_c)
    x = 0
    y = 0
    ans = 0
    min_num = 10000
    min_start = 0

    for q in range(100):
        cnt = 0
        if ladder[0][q] == 1:
            x = 0
            y = q
            # if q  < 50:
            #     cnt += q
            # else :
            #     cnt += (99 - q)

            while (x != 99):
                if y == 0:  # 맨 왼쪽
                    if ladder[x][y + 1] == 1:
                        y += 1
                        cnt += 1
                        while ladder[x + 1][y] == 0:
                            y += 1
                            cnt += 1
                        x += 1
                        cnt += 1
                    else:
                        x += 1
                        cnt += 1

                elif y == 99:  # 맨 오른쪽
                    if ladder[x][y - 1] == 1:
                        y -= 1
                        cnt += 1
                        while ladder[x + 1][y] == 0:
                            y -= 1
                            cnt += 1
                        x += 1
                        cnt += 1
                    else:
                        x += 1
                        cnt += 1

                else:  # 가운데 어딘가가
                    if ladder[x][y + 1] == 1:  #
                        y += 1
                        cnt += 1
                        while ladder[x + 1][y] == 0:
                            y += 1
                            cnt += 1
                        x += 1
                        cnt += 1

                    elif ladder[x][y - 1] == 1:
                        y -= 1
                        cnt += 1
                        while ladder[x + 1][y] == 0:
                            y -= 1
                            cnt += 1
                        x += 1
                        cnt += 1
                    else:
                        x += 1
                        cnt += 1
            # print(q, cnt)
            #print(f'#{tc} #{q} {cnt}')
            if min_num >= cnt:
                min_num = cnt
                min_start = q
    print(f'#{tc} {min_start}')
