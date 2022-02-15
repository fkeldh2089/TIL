# 2669 직사각형 네개의 합집합의 면적 구하기
import sys
sys.stdin = open('input_2669.txt')

# 2차원으로 두고 생각을 하자, 100 by 100 밖에 안된다

mat = [[0]*100 for _ in range(100)]  # 평면 생성
xy = []  # 저장할 좌표들
for p in range(4):  # 직사각형 4개
    col = list(map(int, input().split()))
    xy.append(col)

de_area = 0  # 넓이 다 더한 것
cnt = 0
for t in range(4):  # 직사각형은 4개니깐
    de_area += (xy[t][2] - xy[t][0]) * (xy[t][3] - xy[t][1])
    for p1 in range(xy[t][0], xy[t][2]):  # 가로 길이 만큼 반복
        for p2 in range(xy[t][1], xy[t][3]):  # 세로 길이 만큼 반복
            mat[p1][p2] += 1  # 차지하는 영역에 1더해줌
            if mat[p1][p2] >= 2:  # 만약 겹쳐있다면 카운트
                cnt += 1


print(de_area - cnt)