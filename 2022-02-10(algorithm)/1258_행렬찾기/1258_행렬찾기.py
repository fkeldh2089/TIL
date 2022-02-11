# 1258 행렬 찾기
import sys
sys.stdin = open('input_1258.txt')

TC = int(input())

def sear_box(n, field):
    ans = []
    for q in range(n):
        f = 0  # 플래그
        cnt = 0

        # 가로의 길이들만 구해준다
        for p in range(n):
            if field[q][p] != 0:  # 0이 아닌 숫자가 오면 cnt +, 플래그 1
                f = 1
                cnt += 1

            else:  # 0일 경우
                if f == 1:  # 숫자가 0이 된 것이면, cnt 추가 후 리셋
                    ans.append(cnt)
                    f = 0
                    cnt = 0
            if p == (n-1) and cnt != 0: # 마지막이 0이 아닐 경우
                ans.append(cnt)
                cnt = 0

    # 최대 길이 계산
    temp_max = 0
    for p in ans:
        if temp_max <= p:
            temp_max = p

    temp_col = [0]*(temp_max + 1)
    for p in range(temp_max + 1):  # 중복되는 행의 길이가 없다고 했으므로,,, 같은 길이끼리 모아버린다.
        for q in range(len(ans)):  # index가 가로 길이, value가 세로길이인 리스트 작성
            if p == ans[q]:
                temp_col[p] += 1

    boxes = []  # 상자들의 가로세로, 넓이를 저장할 리스트
    for p in range(temp_max + 1):
        if temp_col[p] != 0:  # 0이 아니라면,
            boxes.append([p*temp_col[p], temp_col[p], p])  # 박스 리스트에 추가

    # 박스 리스트 길이 구하기
    lenofbox = 0
    for p in boxes:
        lenofbox += 1

    # 크기 순으로 정리
    for p in range(lenofbox):
        for p1 in range(lenofbox - p - 1):
            if boxes[p1] > boxes[p1 + 1]:
                boxes[p1 + 1], boxes[p1] = boxes[p1], boxes[p1 + 1]

    # 넓이 뺴고 문자열로 정리
    boxbox = [str(lenofbox)]
    for p in range(lenofbox):
        boxbox.append(str(boxes[p][1]))
        boxbox.append(str(boxes[p][2]))
    boxbox = ' '.join(boxbox)
    return boxbox



for p in range(TC):
    N = int(input())
    container = []
    for q in range(N):
        chemics = list(map(int, input().split()))
        container.append(chemics)



    print(f'#{p+1} {sear_box(N, container)}')
