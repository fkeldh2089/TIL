# 1220 Magnetic
import sys
sys.stdin = open('input_1220.txt')

def magnetic(n, mfield):
    cnt_sum = 0
    for q in range(n):
        f = 1  # 플래그
        cnt = 0
        for p in range(n):
            if mfield[p][q] == 1:
                if f == 1:
                    f = 2
            elif mfield[p][q] == 2:  # 1 다음에 2가 오면 cnt 증가
                if f == 2:  # 2가 연속되면 cnt증가는 되지 않음
                    cnt += 1
                    f = 1
        cnt_sum += cnt
    return cnt_sum


for p in range(10):
    N = int(input())
    mfield = []
    for q in range(N):
        field_num = list(map(int, input().split()))
        mfield.append(field_num)
    print(f'#{p+1} {magnetic(N,mfield)}')