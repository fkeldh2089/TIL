# 부분집합의 합
import sys
sys.stdin = open('input_ex2.txt')

tc = int(input())
for p in range(tc):
    arr = list(map(int, input().split()))
    cnt = 0  # 조건에 맞는 부분집합 갯수
    for q in range(1 << len(arr)):
        tmp = 0  # 부분집합의 합
        for q1 in range(len(arr)):
            if q & (1 << q1):
                tmp += arr[q1]

        if tmp == 0:
            cnt += 1

    # 여기서 공집합은 부분집합이 아니라고 가정하는 듯
    print(f'#{p+1} {int(cnt>1)}')