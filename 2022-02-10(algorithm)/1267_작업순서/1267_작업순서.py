# 1267 작업순서
import sys
sys.stdin = open('input_1267.txt')

for p in range(10):
    V, E = input().split()
    V = int(V)
    E = int(E)
    nums = list(map(int, input().split()))

    lines = []
    for q in range(E):
        lines.append([nums[2*q], nums[2*q + 1]])

    order = []
    cnt = 0
    while(cnt < V):
        for q1 in range(V):
            for q2 in range(E):
                if (q1+1) == lines[q2]:
                    break
            else:
                order.append(q1+1)
                cnt += 1



    ans = ' '.join(list(map(str, order)))
    print(f'#{p+1} {ans}')