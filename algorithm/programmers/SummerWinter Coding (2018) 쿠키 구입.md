# Summer/Winter Coding (~2018) 쿠키 구입

```python
def solution(cookie):
    answer = -1
    cookie.append(0)
    i1 = 0
    i2 = 0
    l1 = 1
    l2 = 1
    mn = 0
    for q in range(len(cookie)-2):
        i1, i2 = q, q
        l1, l2 = i1+1, i1+1
        i_sum = cookie[i2]
        l_sum = cookie[l2]
        while i2 >= 0 and l2 < len(cookie)-1:
            # print(i_sum, l_sum)
            if i_sum == l_sum:
                if i_sum > mn:
                    mn = i_sum
                i2 -= 1
                l2 += 1
                i_sum += cookie[i2]
                l_sum += cookie[l2]
            elif i_sum < l_sum:
                i2 -= 1
                i_sum += cookie[i2]
            elif i_sum > l_sum:
                l2 += 1
                l_sum += cookie[l2]
        # print(i_sum, l_sum)
        # print(mn)
    return mn
'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.06ms, 10.3MB)
테스트 3 〉	통과 (0.12ms, 10MB)
테스트 4 〉	통과 (0.11ms, 10.4MB)
테스트 5 〉	통과 (0.28ms, 10.2MB)
테스트 6 〉	통과 (14.08ms, 10.2MB)
테스트 7 〉	통과 (18.08ms, 10.3MB)
테스트 8 〉	통과 (33.11ms, 10.2MB)
테스트 9 〉	통과 (82.86ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.3MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (1.00ms, 10.3MB)
테스트 15 〉	통과 (0.84ms, 10.1MB)
테스트 16 〉	통과 (0.82ms, 10.2MB)
테스트 17 〉	통과 (0.87ms, 10.2MB)
테스트 18 〉	통과 (0.88ms, 10.2MB)
테스트 19 〉	통과 (0.74ms, 10.2MB)
테스트 20 〉	통과 (0.76ms, 10.2MB)
테스트 21 〉	통과 (0.98ms, 10MB)
테스트 22 〉	통과 (0.22ms, 10.3MB)
테스트 23 〉	통과 (61.70ms, 10.2MB)
테스트 24 〉	통과 (0.78ms, 10.2MB)
테스트 25 〉	통과 (0.86ms, 10.3MB)
테스트 26 〉	통과 (60.83ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (67.44ms, 10.2MB)
테스트 2 〉	통과 (62.98ms, 10.3MB)
테스트 3 〉	통과 (98.91ms, 10.3MB)
테스트 4 〉	통과 (100.92ms, 10.2MB)
테스트 5 〉	통과 (100.98ms, 10.2MB)
테스트 6 〉	통과 (318.92ms, 10.2MB)
테스트 7 〉	통과 (328.78ms, 10.2MB)
테스트 8 〉	통과 (345.67ms, 10.2MB)
'''
```

