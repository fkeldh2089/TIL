def comp(answer, info):
    cnt = 0
    for p in range(11):
        if info[p] >= answer[p] and info[p]:
            cnt -= 10 - p
        elif info[p] < answer[p]:
            cnt += 10 - p
    return cnt


def Tree(n, p, stack, obj):
    if p == 10:
        stack[10 - obj[p][1]] = n
        n = 0
    if n == 0:
        tmp = comp(stack)
        if mn > tmp:
            baker = [stack]
        if mn == tmp:
            baker.append(stack)
    if n >= obj[p][2]:
        for q in range(2):
            if q:
                n -= obj[p][2]
                stack[10 - obj[p][1]] = obj[p][2]
                p += 1
                Tree(n, p, stack, obj)
            else:
                p += 1
                Tree(n, p, stack, obj)
                pass


def solution(n, info):
    globals()mn = 70
    baker = []
    obj = [[0, 0, 0] for _ in range(11)]  # [평점, 점수, 갯수]
    answer = [0] * 11
    stack = [0] * 11
    for p in range(11):
        if info[p]:
            obj[p] = [2 * (10 - p) / (info[p] + 1), 10 - p, info[p] + 1]
        else:
            obj[p] = [10 - p, 10 - p, 1]
    obj.sort(reverse=True)
    Tree(n, 0, stack, obj)
    #     for p in range(11):
    #         if n >= obj[p][2]:
    #             n -= obj[p][2]
    #             answer[10-obj[p][1]] = obj[p][2]
    #     else:
    #         answer[10] = n

    #     cnt = 0
    #     for p in range(11):
    #         if info[p] >= answer[p] and info[p]:
    #             cnt -= 10 - p
    #         elif info[p] < answer[p]:
    #             cnt += 10 - p

    #     if cnt<0:
    #         answer = [-1]

    return answer

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))