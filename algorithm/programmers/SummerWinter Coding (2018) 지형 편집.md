# Summer/Winter Coding (~2018) 지형 편집

```python
from collections import defaultdict

def solution(land, P, Q):
    answer = 10000000000000000000000
    he = defaultdict(int)
    for p in land:
        for q in p:
            he[q] += 1
    # print(he)
    k1 = []
    for p in he.items():
        k1.append(p)
    k1.sort()
    # print(k1)
    for f in k1:
        fl = f[0]
        tmp = 0
        # print(f'*{fl}')
        for p in he.items():
            # print(p)
            if (fl - p[0])>0:
                tmp += (fl - p[0]) * P * p[1]
            elif (fl-p[0]) <0:
                tmp += (p[0]-fl) * Q * p[1]
            # print(tmp)
        if tmp > answer:
            break
        answer = min(tmp, answer)
        
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.5MB)
테스트 2 〉	통과 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.5MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.5MB)
테스트 6 〉	통과 (0.02ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.5MB)
테스트 8 〉	통과 (0.01ms, 10.4MB)
테스트 9 〉	통과 (0.01ms, 10.4MB)
테스트 10 〉	통과 (0.02ms, 10.5MB)
테스트 11 〉	통과 (1.18ms, 10.4MB)
테스트 12 〉	통과 (7.55ms, 10.4MB)
테스트 13 〉	통과 (36.16ms, 10.5MB)
테스트 14 〉	통과 (257.65ms, 10.7MB)
테스트 15 〉	통과 (2634.81ms, 10.9MB)
테스트 16 〉	통과 (6657.22ms, 11.2MB)
테스트 17 〉	통과 (6341.90ms, 11.2MB)
테스트 18 〉	통과 (7664.38ms, 11.3MB)
테스트 19 〉	통과 (9216.81ms, 11.4MB)
테스트 20 〉	통과 (9913.75ms, 11.6MB)
테스트 21 〉	통과 (0.02ms, 10.4MB)
테스트 22 〉	통과 (0.01ms, 10.4MB)
테스트 23 〉	통과 (0.01ms, 10.3MB)
테스트 24 〉	통과 (0.02ms, 10.3MB)
테스트 25 〉	통과 (0.03ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.03ms, 10.3MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.5MB)
테스트 30 〉	통과 (0.01ms, 10.4MB)
테스트 31 〉	통과 (0.01ms, 10.4MB)
테스트 32 〉	통과 (0.01ms, 10.5MB)
효율성  테스트
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
테스트 6 〉	통과 (6.23ms, 11MB)
테스트 7 〉	통과 (7.49ms, 14.1MB)
테스트 8 〉	실패 (시간 초과)
'''
```

- 시간 초과

```python
from collections import defaultdict

def solution(land, P, Q):
    answer = 0
    he = defaultdict(int)
    block_tmp = 0  # 총 블록 개수
    for p in land:
        for q in p:
            he[q] += 1
            block_tmp += 1
    block_sum = block_tmp

    k1 = []
    for p in he.items():
        k1.append(p)
    k1.sort()
    
    tmp = 0  # 첫째층으로 깎고 시작,
    fl =k1[0][0]  # 첫번째 층
    for p in k1:
        tmp += (p[0] - fl)*Q*p[1]
    answer = tmp
    
    for p in range(1, len(k1)):
        # print(tmp)
        block_sum -= k1[p-1][1]  # 아랫층을 제외한 블록 갯수
        # print(block_sum)
        # print(f' 수복: {(block_sum*Q)*(k1[p][0]-k1[p-1][0])}')
        # print(f' 갱신: {(block_tmp-block_sum) * (k1[p][0]-k1[p-1][0]) * P}')
        tmp -= (block_sum*Q)*(k1[p][0]-k1[p-1][0])  # 지웠던 비용 ctrl z
        tmp += (block_tmp-block_sum) * (k1[p][0]-k1[p-1][0]) * P  # 쌓아 올리는 비용

        if tmp > answer:
            break
        answer = min(tmp, answer)
        
    return answer
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.4MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.3MB)
테스트 9 〉	통과 (0.01ms, 10.3MB)
테스트 10 〉	통과 (0.02ms, 10.3MB)
테스트 11 〉	통과 (0.09ms, 10.3MB)
테스트 12 〉	통과 (0.21ms, 10.3MB)
테스트 13 〉	통과 (0.52ms, 10.3MB)
테스트 14 〉	통과 (1.77ms, 10.5MB)
테스트 15 〉	통과 (4.61ms, 10.6MB)
테스트 16 〉	통과 (8.21ms, 11MB)
테스트 17 〉	통과 (8.30ms, 11.1MB)
테스트 18 〉	통과 (9.23ms, 11.1MB)
테스트 19 〉	통과 (10.84ms, 11.3MB)
테스트 20 〉	통과 (9.92ms, 11.4MB)
테스트 21 〉	통과 (0.02ms, 10.2MB)
테스트 22 〉	통과 (0.01ms, 10.4MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.02ms, 10.4MB)
테스트 25 〉	통과 (0.02ms, 10.2MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.02ms, 10.3MB)
테스트 28 〉	통과 (0.01ms, 10.3MB)
테스트 29 〉	통과 (0.02ms, 10.3MB)
테스트 30 〉	통과 (0.01ms, 10.2MB)
테스트 31 〉	통과 (0.01ms, 10.4MB)
테스트 32 〉	통과 (0.01ms, 10.3MB)
효율성  테스트
테스트 1 〉	통과 (139.93ms, 25MB)
테스트 2 〉	통과 (129.64ms, 25MB)
테스트 3 〉	통과 (109.68ms, 24.6MB)
테스트 4 〉	통과 (73.65ms, 22.1MB)
테스트 5 〉	통과 (71.73ms, 24.9MB)
테스트 6 〉	통과 (8.38ms, 10.9MB)
테스트 7 〉	통과 (10.28ms, 13.8MB)
테스트 8 〉	통과 (133.98ms, 21.8MB)
'''
```

