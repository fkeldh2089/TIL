# 1218 String
import sys
sys.stdin = open('input_1213.txt', encoding='utf-8')


for k in range(10):
    TC = int(input())  # 테스트 케이스 번호
    OB = input()
    ST = input()

    cnt = 0
    for p in range(len(ST)-len(OB) + 1):
        if OB == ST[p:p+len(OB)]:
            cnt += 1

    print(f'#{TC} {cnt}')
