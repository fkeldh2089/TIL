## Brute force

- 시각화

  https://zhengqijun0121.github.io/blog/html/visualization/BF.html

```python
def brute_force_for(p, t):
    N = len(t)
    M = len(p)

    # 시작 위치 컨트롤
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j]:
                break
        else:
            return i
    return -1
```

## KMP

- 시각화

  https://cmps-people.ok.ubc.ca/ylucet/DS/KnuthMorrisPratt.html

```python
# T : target / P : pattern

def pre_process(P):

    M = len(P)
    lps = [0] * len(P)

    j = 0
    # pattern의 가장 앞을 제외하고, 매칭이 실패했을 때 돌아갈 곳을 계산한 리스트를 만들어줍니다.

    # i : pattern에서 지나가고 있는 idx
    # j : 지나가고 있는 idx와 pattern의 앞부분과 같은 부분에 대한 idx

    for i in range(1, M):
        # i 와 j가 같으면 lps의 i 자리에 j+1을 넣어줍니다
        if P[i] == P[j]:
            lps[i] = j + 1
            j += 1
        # 다르다면, j를 초기화 해주어 pattern의 가장 처음부터 인식하도록 합니다.
        # 그 자리에서 기존의 j자리(비교를 하고 있던 자리)가 아닌 pattern 처음으로 돌아가 비교를 해줍니다.
        else:
            j = 0
            if P[i] == P[j]:
                lps[i] = j + 1
                j += 1

    # 위와 동일한 코드
    # if P[i] != P[j]:
    #     j = 0
    # if P[i] == P[j]:
    #     lps[i] = j + 1
    #     j += 1

    return lps

def KMP(T, P, lps):

    N = len(T)
    M = len(P)

    # i : target을 도는 위치
    # j : pattern을 도는 위치
    i, j = 0, 0
    pos = -1

    # i 가 target 전체를 돌때 까지
    while i < N:
        # target과 pattern이 맞으면 둘의 index를 += 1
        if P[j] == T[i]:
            i += 1
            j += 1
        # 다르다면
        else:
            # j의 위치를 이전 패턴의 위치로 바꿔준다.
            # 만약 j가 0이라면, 더이상 pattern 안에서 찾을 수 없으므로 i를 하나 증가시킨다.
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        # j가 M에 다다르면, 멈춘다
        if j == M:
            pos = i - j
            break

    return pos

T = 'abcdabeeababcdabcef'
P = 'abcdabcef'

N = len(T)
M = len(P)

lps = pre_process(P)
print(lps)

pos = KMP(T, P, lps)
print(pos)
```

## 보이어-무어

```python
def pre_process(P):

    M = len(P)

    # ASCII 총 개수
    ASCII = 128

    # 배열의 크기를 아스키 코드 + 1개만큼 만들어 준다.
    # 이때, 다른 모든 문자에는 Pattern의 길이 M을 넣어준다
    PI = [M] * (ASCII + 1)

    # skip배열을 만들어준다
    for i in range(M):
        PI[ord(P[i])] = M - 1 - i
    return PI

def boyer_moore(T, P, PI):
    # T : target / P : pattern

    N = len(T)
    M = len(P)

    # i : target에서 찾기 시작할 문자열의 시작점
    i = 0
    # pos : 찾은 문자열의 시작 위치. 없으면 -1
    pos = -1

    while i <= N - M:
        # j : pattern의 끝점, 뒤에서 앞으로 찾음
        j = M - 1
        # k : target에서 찾기 시작할 문자열의 끝점
        k = i + M - 1
        # 매칭을 더 확인해야 하고 and 둘이 같으면 둘다 왼쪽을 찾음.
        while j >= 0 and P[j] == T[k]:
            j -= 1
            k -= 1
        # 끝까지 찾으면 성공
        if j == -1:
            pos = i
            break
        # 아니라면, 기존의 i에서 target의 끝점(ppt의 초록색 부분)에 해당하는 부분만큼 skip
        i = i + PI[ord(T[i + M - 1])]

    return pos

# Target 문자
T = 'a pattern matching algorithm'

# Pattern 문자
P = 'rithm'

# skip 배열을 만들어줌
PI = pre_process(P)
print(PI)

# target, pattern, skip배열을 인자로 넘김
pos = boyer_moore(T, P, PI)
print(pos)
```