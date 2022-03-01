import sys
sys.stdin = open('input.txt')

for tc in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 출발점 인덱스 찾기
    start_num = []
    cnt = -1
    for start in arr[0]:
        cnt += 1
        if start == 1:
            start_num.append(cnt)

    dr = [0, 0, -1, 1]  # 좌(0), 우(1), 상(2), 하(3)
    dc = [-1, 1, 0, 0]

    # 출발점에서 시작, 아래로 내려가면서 좌우 확인, 좌우 확인하다가 1인 지점에서 회전

    result = 0
    for num in start_num:
        r = 0
        c = 0
        # arr[0][num]  # 출발지점
        c = num
        nr = r + dr[3]  # 한칸 내려감
        nc = c + dc[3]
        r, c = nr, nc
        # for i in range(99):  # 사다리타고 100번 내려가야함. 위에서 한번 내려갔으니까 99번
        while nr < 99:
            if nc == 0 and arr[nr][nc+1] == 1:  # 오른쪽으로 감.
                while nc < 99 and arr[nr][nc+1] == 1:
                    nr = r + dr[1]
                    nc = c + dc[1]
                    r, c = nr, nc
                nr = r + dr[3]  # 한칸 내려감
                nc = c + dc[3]
                r, c = nr, nc

            elif nc == 99 and arr[nr][nc-1] == 1:  # 왼쪽으로 감.
                while nc > 0 and arr[nr][nc-1] == 1:
                    nr = r + dr[0]
                    nc = c + dc[0]
                    r, c = nr, nc
                nr = r + dr[3]  # 한칸 내려감
                nc = c + dc[3]
                r, c = nr, nc

            elif 0 <= nr < 100 and 0 <= nc+1 < 100 and arr[nr][nc+1] == 1:  # 오른쪽에 사다리가 연결되었다면,
                while nc < 99 and arr[nr][nc+1] == 1:  # nc=99가 되면 더 오른쪽으로 갈수가 없기때문에 99가 되면 nc<99가 False가 되므로 while문을 빠져 나올수 있다.
                    nr = r + dr[1]
                    nc = c + dc[1]
                    r, c = nr, nc
                nr = r + dr[3]  # 한칸 내려감
                nc = c + dc[3]
                r, c = nr, nc

            elif 0 <= nr < 100 and 0 <= nc-1 < 100 and arr[nr][nc-1] == 1:  # 왼쪽에 사다리가 연결되었다면,
                while nc > 0 and arr[nr][nc-1] == 1:  # nc=0이 되면 더 왼쪽으로 갈수가 없기때문에 0이 되면 nc>0이 False가 되므로 while문을 빠져 나올수 있다.
                    nr = r + dr[0]
                    nc = c + dc[0]
                    r, c = nr, nc
                nr = r + dr[3]  # 가로로 쭉 직진 한 다음에 한칸 내려가야 한다.
                nc = c + dc[3]
                r, c = nr, nc

            else:
                nr = r + dr[3]  # 한칸 내려감
                nc = c + dc[3]
                r, c = nr, nc

        if arr[nr][nc] == 2:
            result = num

    print(f'#{tc} {result}')