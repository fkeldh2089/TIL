# 3143 가장 빠른 문자열 타이핑
import sys
sys.stdin = open('input_3143.txt')

# TC = int(input())

# for p in range(TC):
#     Sentence, Ob = input().split()
#     M = len(Sentence)
#     N = len(Ob)
#     cnt = 0
#     idx = 0
#     while idx < M:
#         if idx + N - 1 < M:
#             if Sentence[idx:idx+N] == Ob:
#                 cnt += 1
#                 idx += N
#             else:
#                 cnt += 1
#                 idx += 1
#         else:
#             cnt += M-idx
#             idx += M-idx
#
#     print(f'#{p+1} {cnt}')



T = int(input())

for tc in range(1, T + 1):
    A, B = list(map(str, input().split()))

    # 단축기 사용횟수
    cnt = 0

    while len(A) >= len(B):
        tmp = ''
        for i in range(len(B)):
            if A[i] == B[i]:
                tmp += A[i]
        if tmp == B:
            A = A[len(B):]
            cnt += 1
        else:
            A = A[1:]
            cnt += 1
    result = cnt + len(A)
    print(result)










# TC = int(input())
#
# for tc in range(1, TC+1):
#     # T는 테이블, P는 패턴
#     T, P = input().split()
#
#     # 1. T에서 P가 몇개 나오는지 세기
#     cnt = 0
#     result = 0
#     for i in range(len(T)-len(P)+1):
#         if T[i:i+len(P)] == P[:]:
#             cnt += 1
#
#     # 2. 값 계산
#     # result = (반복문 빼고 나머지 개수) + (반복문 개수)
#     result = (len(T)-cnt*len(P)) + cnt
#
#     print(f'#{tc} {result}')