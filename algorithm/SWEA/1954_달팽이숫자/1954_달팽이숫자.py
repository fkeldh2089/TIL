# 1954 달팽이 숫자
import sys
sys.stdin = open('input_1954.txt')

TC = int(input())
for p in range(TC):
    N = int(input())
    house = [[0]*N for _ in range(N)]  # 빈 달팽이 집
    for q in range(N):
        house[0][q] = q + 1  # 첫째줄 채워주고

    pos = [0, N-1]  # 시작 위치
    cnt = N
    for q in range(N - 1):  # 길가면서 채워준다는 느낌
        if q % 2 == 0:
            for q1 in range(N-1-q):
                pos[0] += 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt
            for q1 in range(N-1-q):
                pos[1] -= 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt

        else:
            for q1 in range(N-1-q):
                pos[0] -= 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt
            for q1 in range(N-1-q):
                pos[1] += 1
                cnt += 1
                house[pos[0]][pos[1]] = cnt

    print(f'#{p+1}')
    for q in range(N):
        print(' '.join(list(map(str, house[q]))))

