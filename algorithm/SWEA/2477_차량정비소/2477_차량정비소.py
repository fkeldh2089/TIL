# 2477 차량 정비소
import sys
from collections import deque
sys.stdin = open('input_2477.txt')

TC = int(input())

for p in range(TC):
    # N 접수 창구, M 정비 창구, K방문 고객수, A 이용한 접창, B 이용한 정창
    N, M, K, A, B = map(int, input().split())
    TN = list(map(int, input().split()))
    TM = list(map(int, input().split()))
    customers = deque(map(int, input().split()))
    qu1 = deque()  # 접수 창구 대기열
    qu2 = deque()  # 정비 창구 대기열

    reci = [[0, 0] for _ in range(N)]  # 접수 창구 [시간, 고객번호]
    rest = [[0, 0] for _ in range(M)]  # 정비 창구 [시간, 고객번호]
    nums = [[0, 0] for _ in range(K)]  # 고객이 이용한 창구 번호 [접수, 정비]
    t = tmp = customers.popleft() # 가장 먼저온 고객의 시각
    i = 2  # 고객번호
    qu1.append(1)
    f = 0
    # 시간의 흐름에 따라 풀어나가자
    while f == 0:
        while customers and t == customers[0]:  # 그 시각에 고객이 있으면
            customers.popleft()  # 날리고
            qu1.append(i)  # 대기열에 추가
            i += 1
        while qu1:
            for q in range(N):
                if qu1 and reci[q][0] == 0:  # 비어있는 접수처가 있다면,
                    tmp = qu1.popleft()  # 고객 번호 tmp
                    reci[q][0] += TN[q]  # 소요 시간을 더해 준다.
                    reci[q][1] += tmp  # 고객 번호
                    nums[tmp-1][0] += q+1  # 접수 창구 번호
            else:  # 비어있는 창구가 없으면 대기열에 내버려 둔다.
                break

        t += 1  # 시간 흐름
        for q in range(N):
            if reci[q][0] != 0:  # 접수 창구에서 사람이 있다면,
                reci[q][0] -= 1  # 시간이 흐름
                if reci[q][0] == 0:  # 만약 소요 시간이 0이 된다면
                    tmp = reci[q][1]  # 고객 번호 받아두고,
                    reci[q][1] = 0  # 접수 창구 고객번호 클리어
                    qu2.append(tmp)  # 정비 창구 대기열에 넣어준다.
        for q in range(M):
            if rest[q][0] != 0:  # 정비 창구에서 사람이 있다면,
                rest[q][0] -= 1  # 시간이 흐름
                if rest[q][0] == 0:  # 만약 소요 시간이 0이 된다면
                    rest[q][1] = 0  # 정비 창구 고객번호 클리어

        while qu2:
            for q in range(M):
                if qu2 and rest[q][0] == 0:  # 비어있는 정비 창구가 있다면,
                    tmp = qu2.popleft()  # 고객 번호 tmp
                    rest[q][0] += TM[q]  # 소요 시간을 더해 준다.
                    rest[q][1] += tmp  # 고객 번호
                    nums[tmp-1][1] += q+1  # 접수 창구 번호
            else:  # 비어있는 창구가 없으면 대기열에 내버려 둔다.
                break

        for q in range(K):
            if nums[q][1] == 0:
                f = 0
                break
        else:
            f = 1

    ans = 0
    for q in range(K):
        if nums[q][0] == A and nums[q][1] == B:
            ans += q+1
    if ans == 0:
        ans = -1
    print(f'#{p+1} {ans}')
