# 12098 우주전시회
import sys
sys.stdin = open('input_12098.txt')


def calc_sum(nums, k):
    cnt = 0
    ansb = []
    sum1 = 0

    while cnt < len(nums):
        a = cnt + 1
        tmp = []
        k_c = 0
        tmp.append(a)
        r = 0
        while r < len(nums):
            if nums[r][0] == a:
                tmp.append(nums[r][1])
                a = nums[r][1]
                k_c += 1
                # print(f'#{cnt+1} {tmp}')
                r = 0
            else:
                r += 1
            if k_c == k:
                break
        b = len(set(tmp))

        cnt += 1
        ansb.append(b * cnt)
        # print(f'#{cnt} cococo {ansb}')

    for p in ansb:
        sum1 += p
    return sum1


n = int(input())  # 테스트 케이스 반복
for test_case in range(n):
    nums = input().split()  # 별의 갯수와 이동 횟수 입력
    nums_list = list(map(int, nums))
    Stars = nums_list[0]  # 별 갯수 Stars
    opper = nums_list[1]  # 이동 횟수 opper
    tele_map = []
    for p in range(Stars):
        destination = int(input())
        tele_map.append([p + 1, destination])  # [출발지, 도착지]리스트 생성
    print(f'#{test_case + 1} {calc_sum(tele_map, opper)}')

