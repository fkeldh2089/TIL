# 1952 수영장
import sys
from pprint import pprint
sys.stdin = open('input_1952.txt')
from collections import deque
from copy import deepcopy


def con_price(Quaters, total_price):
    global mn, Q
    if Quaters:
        tmp_total = total_price
        tmp_Quaters = deepcopy(Quaters)
        for k in range(len(Quaters)):
            total_price = tmp_total
            tmp_Q = deepcopy(tmp_Quaters)

            tar = tmp_Q.popleft()  # 가장 작은 달
            # print(k, tar)
            while tmp_Q and tar + 2 >= tmp_Q[0]:  # 큐가 비거나, 가장 작은달 +2 보다 커질때까지,
                tmp_Q.popleft()
            tmp_months = months_price[tar:tar + 3]  # 분기로 잘라서,,
            tmp = 0
            for q1 in tmp_months:
                tmp += q1
            total_price = total_price - tmp + Q
            if total_price < mn:
                mn = total_price
            # print(tmp_Q)
            con_price(tmp_Q, total_price)
            tmp_Quaters.popleft()

    else:
        return 0


TC = int(input())

for p in range(TC):
    # 하루, 한달, 세달, 일년
    D, M, Q, Y = map(int, input().split())
    months = list(map(int, input().split()))
    months_price = []

    for q in months:  # 한달 단위 구하기
        if q*D > M:
            months_price.append(M)
        else:
            months_price.append(q*D)
    total_price = 0
    for q in range(12):
        total_price += months_price[q]

    Quaters = deque()
    for q in range(12):
        tmp_months = months_price[q:q+3]  # 분기로 잘라서,,
        tmp = 0
        for q1 in tmp_months:
            tmp += q1
        if tmp > Q:  # 분기 가격보다 크면,,
            Quaters.append(q)
    # print(f'#{p+1} Quaters {Quaters}')
    mn = total_price
    tmp_total = total_price
    con_price(Quaters, total_price)
    # if Quaters:
    #     tmp_Quaters = deepcopy(Quaters)
    #     for k in range(len(Quaters)):
    #         total_price = tmp_total
    #         while 1:
    #             if Quaters:
    #                 tar = Quaters.popleft()  # 가장 작은 달
    #                 while Quaters and tar + 2 >= Quaters[0]:  # 큐가 비거나, 가장 작은달 +2 보다 커질때까지,
    #                     Quaters.popleft()
    #                 tmp_months = months_price[tar:tar + 3]  # 분기로 잘라서,,
    #                 tmp = 0
    #                 for q1 in tmp_months:
    #                     tmp += q1
    #                 total_price -= tmp
    #                 total_price += Q
    #                 if total_price < mn:
    #                     mn = total_price
    #             else:
    #                 break
    #         tmp_Quaters.popleft()
    #         Quaters = deepcopy(tmp_Quaters)

    if mn > Y:
        mn = Y
    print(f'#{p+1} {mn}')
