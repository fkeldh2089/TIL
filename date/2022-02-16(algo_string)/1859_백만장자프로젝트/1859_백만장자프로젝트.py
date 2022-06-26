# 1859 백만장자프로젝트
import sys
sys.stdin = open('input_1859.txt')


def find_max(n, h):  # 최대 위치 찾기
    ans = 0
    max_height = 0
    for p in range(n):
        if h[p] > max_height:
            max_height = h[p]
            ans = p
    return ans


TC = int(input())
for p in range(TC):
    N = int(input())
    price = list(map(int, input().split()))

    pro = 0  # 수익
    while price:
        d_day = find_max(N, price)  # 최대값 찾고
        sell = price[d_day]  # 가격 찾고
        for q in range(d_day):
            pro += sell - price[q]

        price = price[d_day+1:]  # 최대값인 날 지나고 계속
        N = N -d_day - 1

    print(f'#{p+1} {pro}')
