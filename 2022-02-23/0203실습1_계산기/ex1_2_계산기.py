# ex1-2 계산기
import sys
sys.stdin = open('input_ex1_2.txt')

TC = int(input())

for p in range(TC):
    eq = input()
    ans = []

    for q in eq:
        if q != '+' and q != '*' and q != '/' and q != '-':
            ans.append(int(q))
        elif q == '*':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a1 * a2)
        elif q == '+':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a1 + a2)
        elif q == '/':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a2/a1)
        elif q == '-':
            a1 = ans.pop()
            a2 = ans.pop()
            ans.append(a2-a1)

    ans1 = ans.pop()
    print(f'#{p+1} {ans1}')
