# 1242 암호코드 스캔
import sys
sys.stdin = open('input_1242.txt')

code = {(2, 1, 1): 0,
        (2, 2, 1): 1,
        (1, 2, 2): 2,
        (4, 1, 1): 3,
        (1, 3, 2): 4,
        (2, 3, 1): 5,
        (1, 1, 4): 6,
        (3, 1, 2): 7,
        (2, 1, 3): 8,
        (1, 1, 2): 9}

TC = int(input())

for p in range(TC):
    N, M = map(int, input().split())
    numbers = sorted(list(set([input() for _ in range(N)])))
    visited = []
    numbers.pop(0)  # 뭔 깡이지
    sub_sum = 0

    for j in range(len(numbers)):
        change = bin(int(numbers[j], 16)).rstrip("0").replace('0b', '0'*10)  # 오른쪽 0 지우고
        ans = []
        ns = [0, 0, 0, 0]
        f = 3
        for i in range(len(change) - 1, -1, -1):  # 뒤에서 부터,,
            if ns[3] and change[i] != change[i+1]:
                f -= 1
            ns[f] += 1
            if f == 0:
                n1, n2, n3, n4 = ns
                if change[i - 1] == '1':
                    n = min(n2, n3, n4)
                    ans.append((code[n2 // n, n3 // n, n4 // n]))
                    f = 3
                    ns = [0]*4
                    if len(ans) == 8:
                        odd_num = 0
                        even_num = 0
                        for q in range(4):
                            odd_num += ans[2 * q + 1]
                            even_num += ans[2 * q]
                        answer = 3 * odd_num + even_num
                        if answer % 10 or ans in visited:
                            sub = 0
                        else:
                            sub = odd_num + even_num
                            visited.append(ans)
                        sub_sum += sub
                        ans = []
    print(f'#{p + 1} {sub_sum}')
