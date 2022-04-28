```python
import re

def solution(words, queries):
    answer = []
    for qq in range(len(queries)):
        tmp_str = queries[qq]
        tmp = ''
        for q in tmp_str:
            if q=='?':
                tmp += '.'
            else:
                tmp += q
        cnt = 0
        for q in range(len(words)):
            p = re.compile(tmp)
            if len(tmp)==len(words[q]):
                m = p.match(words[q])
                if m:
                    cnt += 1
        else:
            answer.append(cnt)

    return answer

'''
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (580.06ms, 15.3MB)
테스트 5 〉	통과 (1448.08ms, 21.9MB)
```

````python
import re
from collections import deque

def solution(words, queries):
    answer = []
    for qq in range(len(queries)):
        f = 0
        si = 0
        ei = 0
        for q in range(len(queries[qq])):
            if queries[qq][q] != '?':
                if f == 0:  # 문자열이 시작하는 인덱스
                    si = q
                    ei = q
                    f = 1
                else:  # 문자열이 끝나는 인덱스
                    ei = q
        qu = [queries[qq], si, ei+1]  # [쿼리, 시작 인덱스, 끝 인덱스]
        cnt = 0
        for q in range(len(words)):
            if len(queries[qq])==len(words[q]):
                if words[q][qu[1]:qu[2]] == queries[qq][qu[1]:qu[2]]:
                    cnt += 1
        else:
            answer.append(cnt)

    return answer
'''

테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (68.00ms, 13.4MB)
테스트 5 〉	통과 (76.70ms, 13.6MB)
'''

import re
from collections import deque

def solution(words, queries):
    answer = []
    for qq in range(len(queries)):
        f = 0
        si = 0
        ei = 0
        m = queries[qq]
        lm = len(m)
        if m[0] == '?':
            for q in range(lm):
                if m[-1-q] == '?':
                    si = lm-q
                    ei = lm
                    break
        else:
            for q in range(lm):
                if m[q] == '?':
                    si = 0
                    ei = q
                    break
        cnt = 0
        for q in range(len(words)):
            n = words[q]
            if lm == len(n):
                if n[si:ei] == m[si:ei]:
                    cnt += 1
        else:
            answer.append(cnt)

    return answer

'''
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (18.36ms, 13.5MB)
테스트 5 〉	통과 (33.41ms, 13.7MB)
```
````

```python
import re
from collections import deque

def solution(words, queries):
    answer = []
    for q in range(len(queries)):
        cnt = 0
        if queries[q][0] == '?':
            for q1 in range(len(words)):
                if len(words[q1]) == len(queries[q]):
                    for q2 in range(len(words[q1])):
                        if queries[q][-q2-1] == '?':
                            cnt += 1
                            break
                        if words[q1][-q2-1] != queries[q][-q2-1]:
                            break
                    else:
                        cnt += 1
            answer.append(cnt)

        elif queries[q][-1] == '?':
            for q1 in range(len(words)):
                if len(words[q1]) == len(queries[q]):
                    for q2 in range(len(words[q1])):
                        if queries[q][q2] == '?':
                            cnt += 1
                            break
                        if words[q1][q2] != queries[q][q2]:
                            break
                    else:
                        cnt += 1
            answer.append(cnt)

    return answer
'''
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (691.75ms, 13.4MB)
테스트 5 〉	통과 (111.07ms, 13.7MB)
'''
```

```python
import re
from collections import deque

def solution(words, queries):
    answer = []
    for qq in range(len(queries)):
        cnt = 0
        m = queries[qq]
        lm = len(queries[qq])
        
        for q in range(len(words)):
            n = words[q]
            if lm == len(n):
                if m[0] == '?':
                    for k in range(lm):
                        if m[-1-k] == '?':
                            cnt += 1
                            break
                        elif n[-1-k] != m[-1-k]:
                            break
                    else:
                        cnt += 1
                else:
                    for k in range(lm):
                        if m[k] == '?':
                            cnt += 1
                            break
                        elif n[k] != m[k]:
                            break
                    else:
                        cnt += 1
        else:
            answer.append(cnt)

    return answer
'''
테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	통과 (470.70ms, 13.3MB)
테스트 5 〉	통과 (74.69ms, 13.6MB)
'''
```

