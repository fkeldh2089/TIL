from collections import deque, defaultdict


def solution(n, k, cmd):
    answer = ''
    deleted_ls = deque()
    nums = defaultdict(lambda: [0, 0])
    for p in range(n):
        nums[p] = [p-1, p+1, p]
    for p in range(len(cmd)):
        if cmd[p][0] == "D":
            tmp_m = int(cmd[p][2:])
            for q in range(tmp_m):
                k = nums[k][1]
        elif cmd[p][0] == "U":
            tmp_m = int(cmd[p][2:])
            for q in range(tmp_m):
                k = nums[k][0]
        elif cmd[p][0] == "C":
            nums[nums[k][0]][1] = nums[k][1]
            nums[nums[k][1]][0] = nums[k][0]
            deleted_ls.append(nums[k])
            if nums[k][1] != n:
                k = nums[k][1]
            else:
                k = nums[k][0]
        else:
            tmp = deleted_ls.pop()
            nums[tmp[0]][1] = tmp[2]
            nums[tmp[1]][0] = tmp[2]
    ans = ['O']*n
    for q in range(len(deleted_ls)):
        ans[deleted_ls[q][2]] = 'X'
    answer = ''.join(ans)
    print(answer)
    return answer

n, k = 8, 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

solution(n, k, cmd)