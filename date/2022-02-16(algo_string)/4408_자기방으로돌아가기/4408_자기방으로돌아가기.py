# 4408 자기 방으로 돌아가기
import sys
import math
sys.stdin = open('input_4408.txt')

# 루트가 겹치는 정도만 확인하자
TC = int(input())
for p in range(TC):
    N = int(input())  # 학생 수
    rooms = [0] * 200  # 방
    for q in range(N):
        ST, EN = list(map(int, input().split()))  # 시작 끝 지점
        # 시작 index : x, 끝 index : y
        if ST < EN:
            x = math.ceil(ST/2) - 1
            y = math.ceil(EN/2) - 1
        else:
            y = math.ceil(ST/2) - 1
            x = math.ceil(EN/2) - 1

        for q1 in range(x, y+1):
            rooms[q1] += 1

    ans = rooms[0]
    for q in range(200):
        if ans < rooms[q]:
            ans = rooms[q]
    print(f'#{p+1} {ans}')
