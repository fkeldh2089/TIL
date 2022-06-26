import sys
sys.stdin = open('input_ex2.txt')

TC = int(input())
for p in range(TC):
    cnts = [0]*10
    nums = input()
    for q in nums:
        cnts[int(q)] += 1
    for q in range(10):
        if cnts[q] >= 3:
            cnts[q] = cnts[q] % 3
    for q in range(10):
        if cnts[q] >= 1 and q+2 < 10:
            cnts[q] -= 1
            cnts[q+1] -= 1
            cnts[q+2] -= 1
    if cnts == [0]*10:
        print(True)
    else:
        print(False)