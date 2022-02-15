# 1244 스위치 켜고 끄기
import sys
sys.stdin = open('input_1244.txt')


# 함수로 갑시다.
def boy(n, m, mat):  # n: 받은 수, m: 스위치 수, mat: 스위치 상태
    p = 1
    while(p*n <= m):
        if mat[p*n - 1] == 0:
            mat[p*n - 1] = 1
        else:
            mat[p*n - 1] = 0
        p += 1
    return mat


def girl(n, m, mat):
    p = 0
    while(p + n < m and n - p > 1):
        if mat[n+p] == mat[n-2-p]:  # 양쪽이 같다면
            p += 1
        else:  # 같지 않다면
            break

    for q in range(n-p, p+n+1):  # 교환 과정
        if mat[q - 1] == 0:
            mat[q - 1] = 1
        else:
            mat[q- 1] = 0

    return mat


N = int(input())
switch = list(map(int, input().split()))  # 스위치 리스트
stu_num = int(input())  # 학생 수 받고
for p in range(stu_num):
    S, num = list(map(int, input().split()))  # 학생 정보 받고

    if S == 1:
        switch = boy(num, N, switch)
    else:
        switch = girl(num, N, switch)

# 스위치가 20개 이상이면 줄을 바꿔야 한다네,,
re_print = (N//20) + 1  # 반복 출력할 횟수
for p in range(re_print):
    print(' '.join(list(map(str, switch[20*p:20*(p + 1)]))))

# switch = ' '.join(list(map(str, switch)))
# print(' '.join(list(map(str, switch))))
