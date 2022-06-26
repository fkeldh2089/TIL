# 5789. 현주의 상자 바꾸기
import sys
sys.stdin = open('input_5789.txt')

tc = int(input())

for p in range(tc):
    sets = list(map(int, input().split()))
    set1 = sets[0]
    set2 = sets[1]

    boxes = [0] * set1



    for q in range(set2):
        LR = list(map(int, input().split())) # LR 입력 받고
        L = LR[0]
        R = LR[1]
        boxes[L-1:R] = [q+1]*(R-L+1) # L~R 부분을 i로 변경
        #print(boxes)

    ans = ' '.join(map(str, boxes))
    print(f'#{p+1} {ans}')