# Summer/Winter Coding (~2018) 스티커 모으기(2)

```python
def solution(sticker):
    answer = 0
    visited1 = [0] * len(sticker)
    visited2 = [0] * len(sticker)
    if len(sticker)<3:
        return max(sticker)
    
    visited1[0] = sticker[0]  # 첫번째 요소 뜯고 시작
    visited2[-1] = sticker[-1]  # 마지막 요소 뜯고 시작
    for p in range(len(sticker)):
        visited1[p] = max(visited1[p-1], visited1[p-2] + sticker[p])
    for p in range(len(sticker)):
        visited2[p] = max(visited2[p-1], visited2[p-2] + sticker[p])
    # print(visited1, visited2)
    return max(visited1[-2], visited2[-3])
'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.2MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.02ms, 10MB)
테스트 7 〉	통과 (0.81ms, 10.2MB)
테스트 8 〉	통과 (0.58ms, 10.2MB)
테스트 9 〉	통과 (0.57ms, 10.3MB)
테스트 10 〉	통과 (0.56ms, 10.2MB)
테스트 11 〉	통과 (0.58ms, 10.3MB)
테스트 12 〉	통과 (0.58ms, 10.2MB)
테스트 13 〉	통과 (0.55ms, 10.2MB)
테스트 14 〉	통과 (0.56ms, 10.2MB)
테스트 15 〉	통과 (0.59ms, 10.3MB)
테스트 16 〉	통과 (0.54ms, 10.2MB)
테스트 17 〉	통과 (0.55ms, 10.3MB)
테스트 18 〉	통과 (0.55ms, 10.1MB)
테스트 19 〉	통과 (0.55ms, 10.2MB)
테스트 20 〉	통과 (0.76ms, 10.1MB)
테스트 21 〉	통과 (0.55ms, 10.3MB)
테스트 22 〉	통과 (0.57ms, 10.4MB)
테스트 23 〉	통과 (0.57ms, 10.4MB)
테스트 24 〉	통과 (1.03ms, 10.3MB)
테스트 25 〉	통과 (0.55ms, 10.2MB)
테스트 26 〉	통과 (0.54ms, 10.4MB)
테스트 27 〉	통과 (0.56ms, 10.3MB)
테스트 28 〉	통과 (0.55ms, 10.1MB)
테스트 29 〉	통과 (0.54ms, 10.2MB)
테스트 30 〉	통과 (0.54ms, 10.3MB)
테스트 31 〉	통과 (0.81ms, 10MB)
테스트 32 〉	통과 (0.56ms, 10.2MB)
테스트 33 〉	통과 (0.00ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (58.14ms, 16.5MB)
테스트 2 〉	통과 (61.64ms, 16.6MB)
테스트 3 〉	통과 (59.95ms, 16.5MB)
테스트 4 〉	통과 (61.02ms, 15.9MB)
'''
```

