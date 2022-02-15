import sys
sys.stdin = open('input_2304.txt')


def sort_pill(N, nums):  # 버블 소트
    for q1 in range(N - 1):
        for q2 in range(N - q1 - 1):
            if nums[q2][0] > nums[q2 + 1][0]:
                nums[q2 + 1], nums[q2] = nums[q2], nums[q2 + 1]
    return nums


def find_max(n, h):  # 최대 기둥 위치 찾기
    ans = 0
    max_height = 0
    for p in range(n):
        if h[p][1] > max_height:
            max_height = h[p][1]
            ans = p
    return ans


N = int(input())
pill = []  # 기둥
for p in range(N):
    col = list(map(int, input().split()))
    pill.append(col)
pill = sort_pill(N, pill)  # 순서대로 정렬

max_po = find_max(N, pill)  # 최대 높이의 위치 확인
max_h = pill[0][1]  # 최대 높이(처음 높이)
ex_pos = pill[0][0]
area = 0  # 넓이
for p in range(max_po):  # 전체 최대높이 만나기 전까지
    if pill[p][1] > max_h:  # 최대값 갱신
        area += max_h * (pill[p][0] - ex_pos)
        max_h = pill[p][1]
        ex_pos = pill[p][0]
area += max_h * (pill[max_po][0] - ex_pos)

area += pill[max_po][1]  # 최대 높이 부분

# 뒷부분은 거꾸로
max_h = pill[N-1][1]  # 최대 높이(처음 높이)
ex_pos = pill[N-1][0]
for p in range(N-1, max_po, -1):  # 전체 최대높이 만나기 전까지
    if pill[p][1] > max_h:  # 최대값 갱신
        area += max_h * (ex_pos - pill[p][0])
        max_h = pill[p][1]
        ex_pos = pill[p][0]
area += max_h * (ex_pos - pill[max_po][0] )

print(area)



