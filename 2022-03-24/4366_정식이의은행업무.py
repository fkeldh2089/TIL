# 4366 정식이의 은행 업무
import sys
sys.stdin = open('input_4366.txt')

TC = int(input())

for p in range(TC):
    B = input()
    T = input()

    tmp_B = int(B, 2)
    B_num = []
    for q in range(len(B)):
        if B[-q-1] == '0':
            B_num.append(tmp_B+(2**q))
        else:
            B_num.append(tmp_B-(2**q))
    print(B_num)
    tmp_T = int(T, 3)
    ans = 0
    for q in range(len(T)):
        for q1 in range(len(B_num)):
            if T[-q] == '0':
                if tmp_T + 3**q == B_num[-q1]:
                    ans = B_num[-q1]
                elif tmp_T + 2*3**q == B_num[-q1]:
                    ans = B_num[-q1]
            elif T[-q] == '1':
                if tmp_T + 3**q == B_num[-q1]:
                    ans = B_num[-q1]
                elif tmp_T - 3**q == B_num[-q1]:
                    ans = B_num[-q1]
            elif T[-q] == '2':
                if tmp_T - 3**q == B_num[-q1]:
                    ans = B_num[-q1]
                elif tmp_T - 2*3**q == B_num[-q1]:
                    ans = B_num[-q1]
            if ans:
                break
        if ans:
            break
    print(f'#{p+1} {str(ans)}')