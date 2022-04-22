import numpy


def solution(key, lock):
    answer = False
    N = len(key)
    ob_cnt = 0
    for q1 in range(len(lock)):
        for q2 in range(len(lock)):
            if lock[q1][q2] == 0:
                ob_cnt += 1

    a = numpy.pad(lock, ((N - 1, N - 1), (N - 1, N - 1)), 'constant', constant_values=5)

    for q in range(4):
        key = list(map(list, zip(*key[::-1])))
        for q1 in range(len(a)-N):
            for q2 in range(len(a)-N):
                cnt = 0
                tmp_if = 0
                for qq1 in range(N):
                    for qq2 in range(N):
                        tmp_if = a[q1 + qq1][q2 + qq2] + key[qq1][qq2]
                        if tmp_if == 2:
                            break
                        elif a[q1 + qq1][q2 + qq2] == 0 and key[qq1][qq2] == 1:
                            cnt += 1
                    if tmp_if == 2:
                        break
                if cnt == ob_cnt:
                    return True

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

ans = solution(key, lock)
print(ans)