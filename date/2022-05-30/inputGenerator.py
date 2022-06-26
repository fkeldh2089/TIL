# 노선 수 T(1<=T<=50)
# 각 노선 별로 K, N, M 이 주어지고 M개의 위성 번호가 주어진다.
import random

for T in range(1, 51):
    K = random.randrange(1, 100)
    M = random.randrange(2, 100)
    N = random.randrange(1, M-1)

    print(T)
    print(f'{K} {M} {N}')
    satel = random.sample(range(1, M-1), N)
    satel.sort()
    print(*satel)