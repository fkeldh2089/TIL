# 2805 농작물 수확하기
import sys
sys.stdin = open('input_2805.txt')

TC = int(input())

for p in range(TC):
    N = int(input())
    Rice = []
    for q in range(N):
        col = list(input().split())
        Rice.append(col)

    price = ''  # 값어치의 스트링
    for q in range(N//2+1):  # 올라가는 부분
        for q1 in range(N//2 - q, N//2 + q + 1):
            price += Rice[q][0][q1]

    for q in range(N//2 + 1, N):  # 내려가는 부분
        for q1 in range(q - N//2, N + N//2 - q):
            price += Rice[q][0][q1]

    price_sum = 0
    for q in range(len(price)):  # 숫자화 하여 다 더해준다.
        price_sum += int(price[q])
    print(f'#{p+1} {price_sum}')
