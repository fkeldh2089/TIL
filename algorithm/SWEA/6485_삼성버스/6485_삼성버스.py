# 6485 삼성시의 버스노선
import sys
sys.stdin = open('input_6485.txt')

TC = int(input())
for p in range(TC):
    N = int(input())  # 버스 노선 갯수
    bus_line = []
    for q in range(N):
        bus = list(map(int, input().split()))  # 노선
        bus_line.append(bus)
    stops = int(input())  # 버스 정류장 수

    stop_number = []
    for q in range(stops):
        trash = int(input())  # 쓸모없는 정류장 입력이 아니었네
        stop_number.append(trash)

    bus_stop = [0]*5000  # 주의, 버스정류장 숫자가 아니라 최대 숫자만큼 존재
    for q in range(N):
        for q1 in range(bus_line[q][0]-1, bus_line[q][1]):
            bus_stop[q1] += 1

    ans = ''
    for q in range(stops):
        ans += ' ' + str(bus_stop[stop_number[q]-1])

    print(f'#{p+1}{ans}')