from pprint import pprint


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,2,1,0],[2,2,0,1]]


result = []
pil = [[0] * (n + 1) for _ in range(n+1)]  # 기둥s
boa = [[0] * (n + 1) for _ in range(n+1)]  # 보s


for p in build_frame:
    x, y, a, b = p  # x, y, (기둥, 보), (삭제, 설치)
    if b == 1:
        if a == 0:
            if y == 0 or pil[x][y-1] == 1:
                pil[x][y] = 1
            elif boa[x][y] == 1 or (x and boa[x-1][y]) == 1:
                pil[x][y] = 1
        elif a == 1:
            if pil[x][y-1] == 1 or pil[x+1][y-1] == 1:
                boa[x][y] = 1
            elif 0 < x < n and boa[x-1][y] == 1 and boa[x+1][y] == 1:
                boa[x][y] = 1

    elif b == 0:
        if a == 0:
            if y != n and pil[x][y+1]:  # 위에 기둥 있고, 보 없으면,,
                if boa[x][y] or (x and boa[x-1][y]):
                    pass
                else:
                    continue
            if y != n and boa[x][y+1]:  # 보가 있다면
                if (x and boa[x-1][y+1]) and (x != n and boa[x+1][y+1]):  # 양쪽으로 보 있으면,,
                    pass
                elif x != n and pil[x+1][y]:  # 기둥이 하나 더 있다면,
                    pass
                else:
                    continue
            if y != n and x and boa[x-1][y+1]:
                if (x-1 and boa[x-2][y+1]) and (boa[x][y+1]):
                    pass
                elif boa[x-1][y]:
                    pass
                else:
                    continue
            pil[x][y] = 0
        if a == 1:
            if pil[x][y]:  # 위에 기둥이 있다면,
                if pil[x][y-1]:  # 밑에 기둥이 있거나
                    pass
                elif x and boa[x-1][y]: # 옆에 보가 있거나
                    pass
                else:
                    continue
            if x != n and pil[x+1][y]:  # 오른쪽 위에 기둥이 있거나
                if pil[x+1][y-1]:
                    pass
                elif x+1 != n and boa[x+2][y]:
                    pass
                else:
                    continue
            if x != n and boa[x+1][y]:  # 오른쪽 보 있을 때,
                if pil[x+1][y-1] or boa[x+2][y-1]:
                    pass
                else:
                    continue
            if x and boa[x-1][y]:
                if pil[x-1][y-1] or pil[x][y-1]:
                    pass
                else:
                    continue
            boa[x][y] = 0

for p2 in range(n+1):
    for p1 in range(n+1):
        if pil[p2][p1] == 1:
            result.append([p2, p1, 0])
        if boa[p2][p1] == 1:
            result.append([p2, p1, 1])
print(result)
