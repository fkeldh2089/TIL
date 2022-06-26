# 연습문제 정수를 문자열로 반환
import sys
sys.stdin = open('input_ex2.txt')


def itoa(n):  # 아스키 코드를 활용한 문자열
    ans = ''
    ans_m = '-'
    if n >= 0:
        while n > 0:
            a = n % 10
            ans += chr(a+48)
            n = n//10
        ans = ans[::-1]
        print(ans, type(ans))
    else:
        n = n *(-1)
        while n > 0:
            a = n % 10
            #
            ans += chr(a+48)
            n = n//10
        ans = ans[::-1]
        ans = ans_m + ans
        print(ans, type(ans))


def itoa2(n):  # 문자열을 이용하랍니다
    ans = ''
    ans_m = '-'
    nums = '0123456789'
    if n >= 0:
        while n > 0:
            a = n % 10
            for q in range(10):
                if q == a:
                    ans += nums[q]
            n = n//10
        ans = ans[::-1]
        print(ans, type(ans))
    else:
        n = n *(-1)
        while n > 0:
            a = n % 10
            for q in range(10):
                if q == a:
                    ans += nums[q]
            n = n//10
        ans = ans[::-1]
        ans = ans_m + ans
        print(ans, type(ans))


for p in range(6):
    soot_ja = int(input())
    print(f'#{p+1} ', end='')
    itoa2(soot_ja)