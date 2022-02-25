# 4874 Forth
import sys
sys.stdin = open('input_4874.txt')

TC = int(input())

for p in range(TC):
    eq = input().split()
    eq.pop()  # . 날리기
    ans = []
    ans1 = 0
    for q in eq:
        if q != '+' and q != '*' and q != '/' and q != '-' and q != '.':
            ans.append(int(q))
        else:
            if len(ans) < 2:
                ans1 = 'error'
                break
            else:
                if q == '*':
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
                    ans.append(a2//a1)
                elif q == '-':
                    a1 = ans.pop()
                    a2 = ans.pop()
                    ans.append(a2-a1)

    if len(ans) > 1 or ans1 != 0:
        ans1 = 'error'
    else:
        ans1 = ans.pop()
    print(f'#{p+1} {ans1}')