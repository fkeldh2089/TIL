# 2021 KAKAO 인턴 표 편집

```python
from collections import deque, defaultdict


def solution(n, k, cmd):
    answer = ''
    deleted_ls = deque()
    nums = defaultdict(lambda: [0, 0, 0])  #[이전 항목, 다음 항목, 본인 인덱스]
    for p in range(n):
        nums[p] = [p-1, p+1, p]
    for p in range(len(cmd)):
        if cmd[p][0] == "D":
            tmp_m = int(cmd[p][2:])
            for q in range(tmp_m):  # 주어진 숫자만큼 다음항목으로 이동
                k = nums[k][1]
        elif cmd[p][0] == "U":
            tmp_m = int(cmd[p][2:])
            for q in range(tmp_m):  # 주어진 숫자만큼 이전 항목으로 이동
                k = nums[k][0]
        elif cmd[p][0] == "C":  # 이전 항목과 다음 항목을 잇고 삭제 큐에 추가
            nums[nums[k][0]][1] = nums[k][1]
            nums[nums[k][1]][0] = nums[k][0]
            deleted_ls.append(nums[k])
            if nums[k][1] != n:
                k = nums[k][1]
            else:
                k = nums[k][0]
        else:  # 이전항목과 다음 항목 사이에 끼어듦
            tmp = deleted_ls.pop()
            nums[tmp[0]][1] = tmp[2]
            nums[tmp[1]][0] = tmp[2]
    ans = ['O']*n
    for q in range(len(deleted_ls)):  # 답 처리
        ans[deleted_ls[q][2]] = 'X'
    answer = ''.join(ans)
    return answer

'''
테스트 1 〉	통과 (0.03ms, 10.5MB)
테스트 2 〉	통과 (0.06ms, 10.4MB)
테스트 3 〉	통과 (0.05ms, 10.5MB)
테스트 4 〉	통과 (0.05ms, 10.6MB)
테스트 5 〉	통과 (0.15ms, 10.5MB)
테스트 6 〉	통과 (0.09ms, 10.4MB)
테스트 7 〉	통과 (0.15ms, 10.5MB)
테스트 8 〉	통과 (0.08ms, 10.5MB)
테스트 9 〉	통과 (0.10ms, 10.4MB)
테스트 10 〉	통과 (0.09ms, 10.4MB)
테스트 11 〉	통과 (0.54ms, 10.5MB)
테스트 12 〉	통과 (0.53ms, 10.5MB)
테스트 13 〉	통과 (0.57ms, 10.6MB)
테스트 14 〉	통과 (1.05ms, 10.4MB)
테스트 15 〉	통과 (1.80ms, 10.5MB)
테스트 16 〉	통과 (2.00ms, 10.6MB)
테스트 17 〉	통과 (12.41ms, 10.7MB)
테스트 18 〉	통과 (4.35ms, 10.5MB)
테스트 19 〉	통과 (7.80ms, 10.6MB)
테스트 20 〉	통과 (2.28ms, 10.6MB)
테스트 21 〉	통과 (2.17ms, 10.5MB)
테스트 22 〉	통과 (2.07ms, 10.5MB)
테스트 23 〉	통과 (0.04ms, 10.5MB)
테스트 24 〉	통과 (0.05ms, 10.4MB)
테스트 25 〉	통과 (0.04ms, 10.4MB)
테스트 26 〉	통과 (0.03ms, 10.4MB)
테스트 27 〉	통과 (0.06ms, 10.5MB)
테스트 28 〉	통과 (0.05ms, 10.5MB)
테스트 29 〉	통과 (0.05ms, 10.4MB)
테스트 30 〉	통과 (0.07ms, 10.5MB)
효율성  테스트
테스트 1 〉	통과 (974.96ms, 247MB)
테스트 2 〉	통과 (985.10ms, 246MB)
테스트 3 〉	통과 (996.21ms, 246MB)
테스트 4 〉	통과 (908.91ms, 253MB)
테스트 5 〉	통과 (949.26ms, 253MB)
테스트 6 〉	통과 (938.61ms, 252MB)
테스트 7 〉	통과 (407.48ms, 65MB)
테스트 8 〉	통과 (257.43ms, 77.6MB)
테스트 9 〉	통과 (1019.82ms, 253MB)
테스트 10 〉	통과 (1061.22ms, 253MB)
'''
```

