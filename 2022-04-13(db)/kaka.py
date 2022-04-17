def preorder(n, visited, nodeinfo, nodes_num, twice, ans):
    ans.append(nodeinfo[n][2])
    for q in range(n + 1, nodes_num + 1):
        if nodeinfo[q][0] < nodeinfo[n][0] and twice[nodeinfo[q][2]] == 0:
            visited.append(nodeinfo[q][2])
            twice[nodeinfo[q][2]] = 1
            preorder(q, visited, nodeinfo, nodes_num, twice, ans)


def inorder(n, visited, nodeinfo, nodes_num, twice, ans):
    for q in range(n + 1, nodes_num):
        if nodeinfo[q][0] < nodeinfo[n][0] and twice[nodeinfo[q][2]] == 0:
            visited.append(nodeinfo[q][0])
            inorder(q, visited, nodeinfo, nodes_num, twice, ans)
            visited.pop()

    else:
        for q in range(n + 1, nodes_num):
            if nodeinfo[n][0] < nodeinfo[q][0] and twice[nodeinfo[q][2]] == 0:
                if len(visited)>=2 and visited[-2] < nodeinfo[q][0]:
                    continue
                inorder(q, visited, nodeinfo, nodes_num, twice, ans)
                # twice[nodeinfo[q][2]] = 1
                # ans.append(nodeinfo[q][2])
                # if len(ans) > 1 and ans[-1] == ans[-2]:
                #     ans.pop()
        else:
            if twice[nodeinfo[n][2]] == 0:
                print(nodeinfo[n][2])
                twice[nodeinfo[n][2]] = 1
                ans.append(nodeinfo[n][2])
                if len(ans) > 1 and ans[-1] == ans[-2]:
                    ans.pop()


def solution(nodeinfo):
    nodes_num = len(nodeinfo)
    for q in range(nodes_num):
        nodeinfo[q] += [q + 1]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    nodeinfo1 = [[100000, 100000, 0]] + nodeinfo
    visited = [nodeinfo1[0][2]]
    twice = [0] * (len(nodeinfo) + 1)
    twice[nodeinfo1[0][2]] = 1
    pre_ans = []
    preorder(0, visited, nodeinfo1, nodes_num, twice, pre_ans)

    visited = [nodeinfo[0][2]]
    twice = [0] * (len(nodeinfo)+1)
    in_ans = []
    inorder(0, visited, nodeinfo, nodes_num, twice, in_ans)
    answer = [pre_ans[1:], in_ans]
    return answer


ans = solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])
print(ans)