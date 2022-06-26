import sys
sys.stdin = open('prac1.txt')


def preorder(li1, li2):
    global N
    i = 1
    V = [i]
    twice = [i]
    while 1:
        if li1[i] != 0:
            # print('a')
            V.append(li1[i])
            twice.append(li1[i])
            tmp = li1[i]
            li1[i] = 0
            i = tmp

        elif li1[i] == 0 and li2[i] == 0:
            # print('b')
            if twice:
                i = twice.pop()
            else:
                break

        else:
            # print('c')
            V.append(li2[i])
            twice.append(li2[i])
            tmp = li2[i]
            li2[i] = 0
            i = tmp
        print(V)





N = int(input())
nums = list(map(int, input().split()))

li1 = [0] * (N + 1)
li2 = [0] * (N + 1)

for p in range(len(nums)//2):
    tmp = nums[2*p:2*p+2]
    # print(tmp)
    if li1[tmp[0]] == 0:
        li1[tmp[0]] = tmp[1]
    else:
        li2[tmp[0]] = tmp[1]

print(li1)
print(li2)
preorder(li1, li2)