# 배열 B의 값

```python
# 16971 배열 B의 값
import sys
sys.stdin = open("input_16971.txt")


N, M = map(int, input().split())
vals = []
for p in range(N):
    vals.append(list(map(int, input().split())))

rs = []
cs = []
Rmn1 = 1000*1000*5
Ridx = -1
for p1 in range(N):
    tmp = 0
    for p2 in range(M):
        if p2 == 0 or p2==M-1:
            tmp += vals[p1][p2]
        else:
            tmp += 2* vals[p1][p2]
    if 0<p1 and p1<N-1 and tmp < Rmn1:
        Rmn1 = tmp
        Ridx = p1
    rs.append(tmp)

Cmn1 = 1000*1000*5
Cidx = -1
for p1 in range(M):
    tmp = 0
    for p2 in range(N):
        if p2 == 0 or p2==N-1:
            tmp += vals[p2][p1]
        else:
            tmp += 2* vals[p2][p1]
    if 0<p1 and p1<M-1 and tmp < Cmn1:
        Cmn1 = tmp
        Cidx = p1
    cs.append(tmp)

RD = 0
if Ridx == 0 or Ridx == len(rs)-1:
    RD = 0
    Ridx = 0
    Ridx2 = len(rs)-1
else:
    Rmn = -1000*1000*5
    Ridx2 = len(rs)-1
    if rs[0] > Rmn:
        Rmn = rs[0]
    if rs[-1] > Rmn:
        Rmn = rs[-1]
        Ridx2 = 0
    RD = Rmn - Rmn1
CD = 0
if Cidx == 0 or Cidx == len(cs)-1:
    CD = 0
    Cidx = 0
    Cidx2 = len(cs)-1
else:
    Cmn = -1000*1000*5
    Cidx2 = len(cs)-1
    if cs[0] > Cmn:
        Cmn = cs[0]
    if cs[-1] > Cmn:
        Cmn = cs[-1]
        Cidx2 = 0
    CD = Cmn - Cmn1

if CD<=0 and RD<=0:
    tot = sum(cs)*2 - cs[0] - cs[-1]
elif CD > RD:
    tot = sum(cs)*2 - cs[Cidx] - cs[Cidx2]
else:
    tot = sum(rs)*2 - rs[Ridx] - rs[Ridx2]

print(tot)




```

### 오답 이유

1. 범위 지정 실수(최소 값을 0으로 생각하고 풀었음)