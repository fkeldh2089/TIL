# 4831 전기 버스
import sys
sys.stdin = open('input_4831.txt')

tc = int(input())

for p in range(tc):
    numbs = list(map(int, input().split()))
    k = numbs[0]
    n = numbs[1]
    m = numbs[2]
    stops = list(map(int, input().split()))

    supply_stop = [0] * (n+1)
    for q in range(m):
        supply_stop[stops[q]] = 1 # 표 생성, 충전소 지점에 1

    pos = 0 # 버스의 위치
    cnt = 0
    temp = []

    while(pos < n): # 버스가 종착에 갈떄까지 반복
        temp = []
        if (pos + k) >= n: # 버스 현재 위치에서 종착까지 한번에 갈 수 있을 경우 break
            break

        for q in range(k): # 버스 현재 위치에서 가장 먼 주유소 탐색
            if supply_stop[pos + q + 1] == 1:
                temp.append(pos + q + 1) # 주유소 입력
        if temp == []: # 주유소가 없을 경우 0 출력
            cnt = 0
            break

        pos = temp[-1] # 가장 먼 주유소로 버스 이동
        cnt += 1

    print(f'#{p+1} {cnt}')

