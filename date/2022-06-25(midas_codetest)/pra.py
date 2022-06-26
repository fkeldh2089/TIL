def DFS(s, n, m, a, b, c, d, linked, cnt):
    global ans
    if len(linked) == n:
        ans.append(cnt)
    else:
        for p in range(m):
            if a[p] == s:
                if not b[p] in linked:
                    linked.append(b[p])
                    cnt[0] += c[p]
                    cnt[1] += d[p]
                    tmp = cnt[::]
                    DFS(b[p], n, m, a, b, c, d, linked, tmp)
                    linked.pop()
                    cnt[0] -= c[p]
                    cnt[1] -= d[p]
            elif b[p] == s:
                if not a[p] in linked:
                    linked.append(a[p])
                    cnt[0] += c[p]
                    cnt[1] += d[p]
                    tmp = cnt[::]
                    DFS(a[p], n, m, a, b, c, d, linked, tmp)
                    linked.pop()
                    cnt[0] -= c[p]
                    cnt[1] -= d[p]

ans = []
def solution(n, m, a, b, c, d):
    global ans
    answer = ''
    # 모든 신장 트리를 찾고, 그 가중치를 구한 후, k를 변화 시켜 보자
    # 결국 a+tb 꼴의 값들을 가질 것이고,, 일차 함수가 될듯
    # 각각의 교점을 찾아서 계산하면 될듯
    DFS(1, n, m, a, b, c, d, [1], [0, 0])
    print(ans)
    return answer
solution(2, 2, [1, 1], [2, 2], [0, 1], [1, 0])