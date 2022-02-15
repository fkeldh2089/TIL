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
        lines.append([nums[2*q], nums[2*q + 1]])  # 간선

    # 뒤에 오는 차라리 뒤에오는 갯수를 세?, - 순서가 중요함 안될듯
    # 완전탐색으로 가?
    order = [0] * V   # 뒤에 오는 횟수 카운트
    for q1 in range(V):
        for q2 in range(E):
            if lines[q2][1] == (q1 + 1):
                order[q1] += 1  # 같으면 카운트

    ans = []
    cnt = 0
    while(cnt < V):
        cnt1 = 0
        for q1 in range(V):  # 일단 0부터 답에 추가
            if order[q1] == 0:
                ans.append(q1+1)
                order[q1] -= 1
                cnt1 += 1  # 이번 반복에 늘어난 숫자
        # 한번 추가가 끝나면, 해당 숫자로 시작하는 숫자 카운트 내리고
        for q1 in range(cnt1):
            for q2 in range(E):
                if ans[cnt + q1] == lines[q2][0]:
                    order[lines[q2][1] - 1] -= 1

        cnt += cnt1




    ans = ' '.join(list(map(str, ans)))
    print(f'#{p+1} {ans}')