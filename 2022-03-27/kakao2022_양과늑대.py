def makesheeps(stack, visited, sheep, wolf, info):
    global right, left, mn
    if sheep - wolf <= 0:
        if sheep > mn:
            mn = sheep
        return
    if visited == [1] * (len(visited)):
        if sheep > mn:
            mn = sheep
        return
    else:
        for q in range(len(stack)):
            if visited[left[stack[q]]] == 0 and left[stack[q]] != -1:
                tmp_L = stack[::]
                tmp_VL = visited[::]
                wolf_L = wolf
                sheep_L = sheep
                tmp_VL[left[stack[q]]] = 1
                # print(tmp_VL)
                tmp_L.append(left[stack[q]])
                if info[left[stack[q]]] == 1:
                    wolf_L += 1
                elif info[left[stack[q]]] == 0:
                    sheep_L += 1
                makesheeps(tmp_L, tmp_VL, sheep_L, wolf_L, info)

            if visited[right[stack[q]]] == 0 and right[stack[q]] != -1:
                tmp_R = stack[::]
                tmp_VR = visited[::]
                wolf_R = wolf
                sheep_R = sheep
                tmp_R.append(right[stack[q]])
                tmp_VR[right[stack[q]]] = 1
                # print(tmp_VR)
                if info[right[stack[q]]] == 1:
                    wolf_R += 1
                elif info[right[stack[q]]] == 0:
                    sheep_R += 1
                makesheeps(tmp_R, tmp_VR, sheep_R, wolf_R, info)


mn = 0
right = []
left = []


def solution(info, edges):
    global mn, right, left
    right = [-1] * len(info)
    left = [-1] * len(info)
    answer = 0
    for p in range(len(edges)):
        if left[edges[p][0]] != -1:
            right[edges[p][0]] = edges[p][1]
        else:
            left[edges[p][0]] = edges[p][1]

    stack = [0]
    visited = [0] * len(info)
    sheep = 1
    wolf = 0
    visited[0] = 1
    makesheeps(stack, visited, sheep, wolf, info)
    answer = mn

    return answer

info = [0,0,0,0,0,0,0,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
k = {"a":2, "b":3}
print(max(k))
ans = solution(info, edges)
print(ans)