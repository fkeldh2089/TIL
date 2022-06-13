# 2021 KAKAO 인턴 거리두기 확인하기

```python
from collections import deque


def BFS(r, c, place):  # BFS 돌립니다,, 벽 마주치면 돌아가고, 2 이하에서 P 마주치면 False
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    stack = deque()
    stack.append([r, c, cnt])
    visited = [[0]*5 for _ in range(5)] 
    visited[r][c] = 1
    while stack:
        r, c, cnt = stack.popleft()
        if cnt == 3:
            return True
        for d in range(4):
            nr, nc = r+dr[d], c+dc[d]
            if 0<=nr<5 and 0<=nc<5 and place[nr][nc]!='X' and visited[nr][nc] == 0:
                if place[nr][nc] == 'P' and cnt != 2:
                    return False
                else:
                    stack.append([nr, nc, cnt + 1])
                    visited[nr][nc] = 1
    return True


def solution(places):
    answer = []
    for p in range(5):
        q1 = 0
        q2 = 0
        ans = 1
        while q1<5:
            if places[p][q1][q2] == 'P':
                if BFS(q1, q2, places[p]):
                    pass
                else:
                    ans = 0
                    break
            q2 += 1
            if q2//5:
                q1 += 1
                q2 %= 5
                
        answer.append(ans)
                
                        
    return answer

'''

테스트 1 〉	통과 (0.24ms, 10.2MB)
테스트 2 〉	통과 (0.07ms, 10.4MB)
테스트 3 〉	통과 (0.10ms, 10.2MB)
테스트 4 〉	통과 (0.08ms, 10.3MB)
테스트 5 〉	통과 (0.04ms, 10.4MB)
테스트 6 〉	통과 (0.08ms, 10.3MB)
테스트 7 〉	통과 (0.05ms, 10.3MB)
테스트 8 〉	통과 (0.10ms, 10.2MB)
테스트 9 〉	통과 (0.11ms, 10.3MB)
테스트 10 〉	통과 (0.03ms, 10.4MB)
테스트 11 〉	통과 (0.09ms, 10.4MB)
테스트 12 〉	통과 (0.06ms, 10.3MB)
테스트 13 〉	통과 (0.06ms, 10.3MB)
테스트 14 〉	통과 (0.06ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10.3MB)
테스트 16 〉	통과 (0.08ms, 10.3MB)
테스트 17 〉	통과 (0.06ms, 10.4MB)
테스트 18 〉	통과 (0.07ms, 10.3MB)
테스트 19 〉	통과 (0.06ms, 10.3MB)
테스트 20 〉	통과 (0.05ms, 10.2MB)
테스트 21 〉	통과 (0.03ms, 10.4MB)
테스트 22 〉	통과 (0.09ms, 10.2MB)
테스트 23 〉	통과 (0.03ms, 10.4MB)
테스트 24 〉	통과 (0.02ms, 10.4MB)
테스트 25 〉	통과 (0.02ms, 10.3MB)
테스트 26 〉	통과 (0.02ms, 10.3MB)
테스트 27 〉	통과 (0.05ms, 10.3MB)
테스트 28 〉	통과 (0.06ms, 10.2MB)
테스트 29 〉	통과 (0.05ms, 10.3MB)
테스트 30 〉	통과 (0.04ms, 10.3MB)
테스트 31 〉	통과 (0.07ms, 10.4MB)
'''
```

