# 4835_구간합
test_case = int(input())  # 테스트 케이스 받고
for p in range(test_case):
    input_set = input().split()  # 인풋 받고
    N = int(input_set[0])  # 리스트 몇개짜리인지 받고
    M = int(input_set[1])  # 몇개 연속하여 계산할 것인지 받고
    numbs_list = list(map(int, input().split()))  # 숫자 리스트 받고

    min_sum = float('inf')  # 최소 최대 기본값 정하고
    max_sum = float('-inf')

    """
    f = 0 # 플래그를 통해 한번만 넣어준다
    min_sum = 0
    max_sum = 0
    """

    for q in range(N - M  + 1):  # 구간 정해주고
        sum_temp = 0  # temp 값 초기화
        for r in range(M):  # 연속되는 M개의 숫자에 대하여
            sum_temp += numbs_list[q + r]  # 더해준다
        if sum_temp <= min_sum:  # 작다면 min 값으로
            min_sum = sum_temp
        if sum_temp >= max_sum:  # 크다면 max 값으로
            max_sum = sum_temp
        """
        if f == 0:
            min_sum = sum_temp
            max_sum = sum_temp
            f = 1 
        """

    print(f'#{p + 1} {max_sum - min_sum}')

