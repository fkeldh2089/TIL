# Baby jin
import sys
sys.stdin = open('input_babyjin.txt')

tc = int(input())

for p in range(tc):
    num_c = [0] * 10
    n = input()

    for q in range(6):
        for q1 in range(10):
            if n[q] == str(q1):
                num_c[q1] += 1

    for t in range(2): # 카드가 어차피 6장이므로 2가지 조합만 걸러내면 됨,
        for q in range(10): # 3보다 클경우 3 뺴주고
            if num_c[q] >= 3:
                num_c[q] -= 3

        for q in range(8): # 연속 될경우 1씩 빼주고
            if num_c[q:q+3] == [1, 1, 1]:
                num_c[q:q+3] = [0, 0, 0]
            if num_c[q:q+3] == [2, 2, 2]:
                num_c[q:q+3] = [1, 1, 1]

    print(f'#{p+1} {1 if num_c == [0]*10 else 0}')
    #print(num_c)