import sys

sys.stdin = open('input_1210.txt')


for p in range(10):
    tc = int(input())
    ladder = []
    for q in range(100):
        ladder_c = list(map(int, input().split()))
        ladder.append(ladder_c)
    x = 0
    y = 0
    ans = 0

    for q in range(100):
        if ladder[0][q] == 1:
            x = 0
            y = q
            while(x != 99):
                if y == 0: # 맨 왼쪽
                    if ladder[x][y + 1] == 1:
                        y += 1
                        while ladder[x + 1][y] == 0:
                            y += 1
                        x += 1
                    else:
                        x += 1

                elif y == 99:  # 맨 오른쪽
                    if ladder[x][y - 1] == 1:
                        y -= 1
                        while ladder[x + 1][y] == 0:
                            y -= 1
                        x += 1
                    else:
                        x += 1

                else : # 가운데 어딘가가
                    if ladder[x][y+1] == 1:#
                        y += 1
                        while ladder[x+1][y] == 0:
                            y += 1
                        x += 1

                    elif ladder[x][y-1] == 1:
                        y -= 1
                        while ladder[x+1][y] == 0:
                            y -= 1
                        x += 1
                    else :
                        x += 1

                if ladder[x][y] == 2:
                    ans = q
                    break

            if ladder[x][y] == 2:
                break
    print(f'#{tc} {ans}')
