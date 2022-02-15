# 13300 방 배정
import sys
sys.stdin = open('input_13300.txt')

# N: 학생수, K: 방별 최대 인원수
N, K = list(map(int, input().split()))
students = [[0, 0] for _ in range(6)]  # 6학년, 0은 여자 1은 남자
for p in range(N):
    S, Y = list(map(int, input().split()))  # 성별과, 학년
    students[Y-1][S] += 1

rooms = 0
for p1 in range(2):
    for p2 in range(6):
        rooms += students[p2][p1]//K
        if students[p2][p1] % K != 0:
            rooms += 1

print(rooms)
