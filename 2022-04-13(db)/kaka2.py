nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]


def pre_order(node):
    if node != 0:
        ans1.append(node)
        pre_order(ll[node])
        pre_order(rr[node])


def post_order(node):
    if node != 0:
        post_order(ll[node])
        post_order(rr[node])
        ans2.append(node)


nodes_num = len(nodeinfo)
for q in range(nodes_num):
    nodeinfo[q] += [q + 1]
nodeinfo.sort(key=lambda x: (-x[1], x[0]))
ll = [0] * (nodes_num + 1)
rr = [0] * (nodes_num + 1)
node_dic = {}
for x, y, idx in nodeinfo:
    node_dic[idx] = [x, y, None, None]
    curr = nodeinfo[0][2]
    while True:
        if x > node_dic[curr][0]:
            if not(node_dic[curr][3]):
                node_dic[curr][3] = idx
                rr[curr] = idx
                break
            curr = node_dic[curr][3]
        elif x < node_dic[curr][0]:
            if not(node_dic[curr][2]):
                node_dic[curr][2] = idx
                ll[curr] = idx
                break
            curr = node_dic[curr][2]
        else:
            break
ans1 = []
pre_order(nodeinfo[0][2])
ans2 = []
post_order(nodeinfo[0][2])
print(ans1, ans2)
