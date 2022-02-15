# 2635 수 이어가기
import sys
sys.stdin = open('input_2635.txt')

N = int(input())
max_num = 0

for p in range(1, N + 1):  # 두번째 수는 N보다 작아야한다.
    f = 0  # 플래그
    cnt = 2
    numbers = [N, p]
    while(f == 0):
        new_num = numbers[-2] - numbers[-1]
        if new_num >= 0:
            numbers.append(new_num)
            cnt += 1

        else:  # 새로운 숫자가 0보다 작으면,,,
            f = 1

    if max_num < cnt:
        max_num = cnt
        max_list = numbers
        ans = cnt

max_list = ' '.join(list(map(str, max_list)))
print(ans)
print(max_list)

