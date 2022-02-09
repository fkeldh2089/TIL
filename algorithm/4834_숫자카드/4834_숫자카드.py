# 4834_숫자카드
import sys

sys.stdin = open('input_4834.txt')

test_case = int(input())
for p in range(test_case):
    input_set = int(input())
    input_num = int(input())
    num_list = [0] * 11
    max_index = 0
    max_num = 0
    for q in range(input_set):
        num_list[input_num % 10] += 1
        input_num = input_num // 10
    # print(num_list)
    for q in range(11):
        if max_num <= num_list[q]:
            max_index = q
            max_num = num_list[q]
    if max_num == 1:
        for q in range(11):
            if num_list[q] == 1:
                max_index = q

    print(f'#{p + 1} {max_index} {max_num}')
