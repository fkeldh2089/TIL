# 19940 피자오븐
import sys
sys.stdin = open("input_19940.txt")



from collections import deque, defaultdict


def getAns(N):
    dp = defaultdict(lambda: 100000000)
    dp[0] = 0
    q = deque()
    q.append([0, 0, 0, 0, 0, 0])
    times = [60, 10, -10, +1, -1]
    while q:
        a, b, c, d, e, idx = q.pop()
        for p in range(4, -1, -1):
            if idx+times[p]<N+70 and idx+times[p]>0:
                if dp[idx]+1 < dp[idx+times[p]]:
                    nextimes = [a, b, c, d, e]
                    nextimes[p] += 1
                    if idx+times[p]==N:
                        return nextimes
                    else:
                        q.appendleft(nextimes+[idx+times[p]])
                        dp[idx+times[p]] = dp[idx]+1
    return [0, 0, 0, 0, 0]

TC = int(input())
for tc in range(TC):
    N = int(input())
    # print()
    ans = [0, 0, 0, 0, 0]
    # 60 쪼개고
    ans[0] += N//60
    N -= ans[0]*60
    ret = getAns(N)
    ret[0] += ans[0]
    for p in range(len(ret)):
        print(ret[p], end=" ")
    print()

