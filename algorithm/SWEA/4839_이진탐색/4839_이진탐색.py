# 4839 이진탐색
import sys
sys.stdin = open('input_4839.txt')


def find_page(a, b, c):  # a~b 쪽에서 c를 찾자
    low = a
    upper = b
    cnt = 0
    mid = 0
    while(mid != c):
        mid = (low + upper)//2
        if mid < c:
            low = mid
            cnt += 1
        elif mid > c:
            upper = mid
            cnt += 1
    return cnt


tc = int(input())
for p in range(tc):
    # P 전체 페이지 수, A B 목표 페이지
    P, A, B = list(map(int, input().split()))
    if find_page(1, P, A) < find_page(1, P, B):
        print(f'#{p+1} A')
    elif find_page(1, P, A) > find_page(1, P, B):
        print(f'#{p+1} B')
    else:
        print(f'#{p + 1} 0')