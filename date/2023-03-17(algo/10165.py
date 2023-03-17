import sys
sys.stdin = open("input_10165.txt")


N = int(input())
M = int(input())

ab = []
for p in range(M):
    a, b = map(int, input().split())
    if a < b:
        ab.append((a, b, p))
    else:
        ab.append((a-N,b, p))
        ab.append((a, N+1, p))

ab.sort(key=lambda x: (x[0], -x[1]))

ans = []
mx = -N
print(ab)
for p in range(len(ab)):
    if mx < ab[p][1]:
        # print(p, mx, ab[p][1])
        mx = ab[p][1]
        if mx == N+1:
            break
        if ab[p][1]!=N+1:
            ans.append(str(ab[p][2]+1))
# print(ans)
ans.sort()
ans=' '.join(ans)
print(ans)