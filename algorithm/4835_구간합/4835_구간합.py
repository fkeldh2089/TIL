# 4835_구간합
test_case = int(input())
for p in range(test_case):
    input_set = input().split()
    a = int(input_set[0])
    b = int(input_set[1])
    numbs = input().split()
    numbs_list = list(map(int, numbs))
    min_sum = float('inf')
    max_sum = float('-inf')

    for q in range(a - b + 1):
        sum_temp = 0
        for r in range(b):
            sum_temp += numbs_list[q + r]
        if sum_temp <= min_sum:
            min_sum = sum_temp
        if sum_temp >= max_sum:
            max_sum = sum_temp

    print(f'#{p + 1} {max_sum - min_sum}')

