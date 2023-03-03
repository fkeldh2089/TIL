#1043 거짓말
import sys
sys.stdin = open("input_1043.txt")


from collections import deque


N, M = map(int, input().split())
secretRow = input()
if len(secretRow) == 1:
    n = 0
    print(M)
else:
    secretRow = list(map(int, secretRow.split()))
    n = secretRow[0]
    secPs = secretRow[1:]
    remainParty = [1]*M
    remainPer = [1] *(N+1)
    per_par = {}
    par_per = {}
    for p in range(M):
        par_per.update({p:[]})
        row = input()
        if len(row) == 1:
            row = list(int(row))
        else:
            row = list(map(int, row.split()))[1:]
        for p1 in range(len(row)):
            par_per[p].append(row[p1])
            if per_par.get(row[p1]):
                per_par[row[p1]].append(p)
            else:
                per_par.update({row[p1]:[p]})
    
    q = deque(secPs)
    # print(par_per)
    cnt = 0
    while q:
        curP = q.pop()
        remainPer[curP] = 0
        if per_par.get(curP):
            for p in per_par[curP]:
                if remainParty[p]:
                    remainParty[p] = 0
                    cnt += 1
                    for p1 in par_per[p]:
                        if remainPer[p1]:
                            q.appendleft(p1)
                            remainPer[p1] = 0

    print(M-cnt)

