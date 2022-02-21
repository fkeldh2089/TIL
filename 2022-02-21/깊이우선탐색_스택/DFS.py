# DFS
import sys
sys.stdin = open('input_DFS.txt')


def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow!')
    else:
        stack[top] = item


def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top+1]


def isEmpty():
    global top
    if top == -1:
        return True
    else:
        return False


def peek():
    global top
    if top == -1:
        print('Empty')
    else:
        return stack[top]


def DFS(v):
    visited[v-1] = 1  # v 에서 시작
    ans = []
    ans.append(v)
    push(v, E)
    # print(stack)
    while 1:
        for p in range(2*V):
            if lines[p][0] == v:  # v로 시작한 간선
                w = lines[p][1]
                # print(f'v, w : {v}, {w}')
                if visited[w-1] == 0:  # 방문안한 지점,
                    ans.append(w)
                    visited[w-1] = 1  # 방문 표시
                    push(w, E)  # 스택에 추가
                    # print(stack)
                    v = w
                    # print(v, w)
                    break
        else:
            v = pop()
            # print(visited)
        if visited == [1] * E:
            break
    return ans


E, V = list(map(int, input().split()))
visited = [0] * E
stack = [0] * E
top = -1
line = list(map(int, input().split()))
lines = []
for p in range(V):
    lines.append(line[2*p:2*(p+1)])
    lines.append(line[2 * p:2 * (p + 1)][::-1])
# print(lines)
print(DFS(1))

