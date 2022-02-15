# 4836 색칠하기
import sys
sys.stdin = open('input_4836.txt')

tc = int(input())
for p in range(tc):
    mat = [[0] * 10 for _ in range(10)]  # 평면 생성
    N = int(input())
    xy = []  # 저장할 좌표들
    for q in range(N):  # 직사각형 4개
        col = list(map(int, input().split()))
        xy.append(col)

    cnt = 0
    for t in range(N):  # 직사각형은 4개니깐
        for p1 in range(xy[t][0], xy[t][2] + 1):  # 가로 길이 만큼 반복
            for p2 in range(xy[t][1], xy[t][3] + 1):  # 세로 길이 만큼 반복
                if mat[p1][p2] != xy[t][4]:  # 같은 색이 아니라면,
                    mat[p1][p2] += xy[t][4]  # 차지하는 영역에 색을 더해줌
                    if mat[p1][p2] == 3:  # 보라가 되었을 때 카운트
                        cnt += 1

    print(f'#{p+1} {cnt}')