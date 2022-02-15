# 1860 진기의 최고급 붕어빵
import sys
sys.stdin = open('input_1860.txt')

TC = int(input())

for p in range(TC):
    # N 사람 수, M 시간, K 개수
    N, M, K = list(map(int, input().split()))
    peo = list(map(int, input().split()))  # 사람 오는 시간

    # 게임마냥 만들어 봅시다 - 시간 제한 떔에 안될듯
    fish_pang = 0  # 붕어빵
    flow_time = 0  # 시간
    ans = 'Possible'
    while(flow_time <= max(peo)):  # 영업 종료 전까지
        if flow_time > 0:
            if flow_time%M == 0:  # 붕어빵 시간
                fish_pang += K

        for q in range(N):
            if peo[q] == flow_time:  # 손님이 올 시간이면,,
                fish_pang -= 1  # 붕어삥을 하나 가져갑니다

        if fish_pang < 0:  # 붕어빵이 음수가 된다면
            ans = 'Impossible'
            break  # 장사 끝

        flow_time += 1  # 시간이 하나 흐릅니다.

    print(f'#{p+1} {ans}')
