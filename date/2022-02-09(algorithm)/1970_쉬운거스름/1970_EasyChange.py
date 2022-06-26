import sys

sys.stdin = open('input_1970.txt')

tc = int(input())

for p in range(tc):
    allch = int(input())
    ch_sum = 0
    changes = [0] * 8
    while(ch_sum != allch):
        if allch >= 50000:
            allch -= 50000
            changes[0] += 1
        elif allch >= 10000:
            allch -= 10000
            changes[1] += 1
        elif allch >= 5000:
            allch -= 5000
            changes[2] += 1
        elif allch >= 1000:
            allch -= 1000
            changes[3] += 1
        elif allch >= 500:
            allch -= 500
            changes[4] += 1
        elif allch >= 100:
            allch -= 100
            changes[5] += 1
        elif allch >= 50:
            allch -= 50
            changes[6] += 1
        elif allch >= 10:
            allch -= 10
            changes[7] += 1
        else:
            allch = 0


    print(f'#{p+1}')
    print(' '.join(map(str, changes)))