# 5432 쇠막대기 자르기
import sys
sys.stdin = open('input_5432.txt')

TC = int(input())

for p in range(TC):
    arr = input()
    M = len(arr)

    ans = 0  # 잘린 쇠파이프
    q = 0
    cnt = 0
    while q < M:
        if arr[q] == '(':  # 여는 괄호 만나면 카운트 +
            cnt += 1
            q += 1
            if arr[q] == ')':  # () 연속적으로 나오면,
                cnt -= 1
                ans += cnt
                q += 1

        else:  # 닫는 괄호 단독으로 만나면 카운트 -, 조각도 하나 더해주고
            ans += 1
            cnt -= 1
            q += 1

    print(f'#{p+1} {ans}')
