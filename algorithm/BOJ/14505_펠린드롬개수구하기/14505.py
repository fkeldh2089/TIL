# 14505 펠린드롬 개수 구하기
import sys
sys.stdin = open("input_14505.txt")

S = input()
# ans = 0
# # 홀수
# for p in range(len(S)):
#     idx1 = p
#     idx2 = p
#     while idx1>=0 and idx2<len(S):
#         if S[idx2]==S[idx1]:
#             ans += 1
#             print(S[idx1:idx2+1])
#         else:
#             break
#         idx2 += 1
#         idx1 -= 1

# # 짝수
# for p in range(len(S)-1):
#     idx1 = p
#     idx2 = p+1
#     while idx1>=0 and idx2<len(S):
#         if S[idx2]==S[idx1]:
#             ans += 1
#             print(S[idx1:idx2+1])
#         else:
#             break
#         idx2 += 1
#         idx1 -= 1
# print(ans)

n = len(S)
dp = [[0]*n for _ in range(n)]
for p in range(n):
    dp[p][p] = 1

idx = 0
sup = 1
while sup<n:
    if idx+sup<n:
        if S[idx] == S[idx+sup]:
            dp[idx][idx+sup] = dp[idx+1][idx+sup] + dp[idx][idx+sup-1] + 1
        else:
            dp[idx][idx+sup] = dp[idx+1][idx+sup] + dp[idx][idx+sup-1] - dp[idx+1][idx+sup-1]
        idx += 1
    else:
        idx = 0
        sup += 1
# tot = 0
# for p in range(n):
#     tot += dp[p][-1]
# print(dp)
print(dp[0][-1])