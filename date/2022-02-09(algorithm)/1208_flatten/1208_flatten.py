# 1208_flatten
import sys

sys.stdin = open('input_1208.txt')

for p in range(10):
    opper = int(input())
    boxes = list(map(int, input().split())) # 박스 생성
    box_num = 0 # 박스 숫자

    for q in boxes:
        box_num += 1


    for r in range(opper):
        nb = boxes[0]
        xb = boxes[0]
        temp_min, temp_max = 0, 0
        for q in range(box_num):
            if nb >= boxes[q]:
                nb = boxes[q]
                temp_min = q
            if xb <= boxes[q]:
                xb = boxes[q]
                temp_max = q

        if nb == xb:
            break

        boxes[temp_min] += 1
        boxes[temp_max] -= 1

    nb = boxes[0]
    xb = boxes[0]
    for q in range(box_num):
        if nb >= boxes[q]:
            nb = boxes[q]
        if xb <= boxes[q]:
            xb = boxes[q]

    print(f'#{p+1} {xb - nb}')
