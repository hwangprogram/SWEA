# 방향값: 1 - 상, 2 - 하, 3 - 좌, 4 -우
dt = ((-1, 0), (1, 0), (0, -1), (0, 1))

T = int(input())

for tc in range(1, T+1):
    # 셀의 크기 NxN, 격리 시간 M, 군집의 개수 K
    N, M, K = map(int, input().split())
    # 미생물들 cells
    cells = []
    # 미생물 군집들 추가
    for _ in range(K):
        cells.append(list(map(int, input().split())))

    # 군집들의 방향들 -1 씩 해주기(인덱스 편의성)
    for cell in cells:
        cell[3] -= 1

    for _ in range(M):
        # 1. 1초마다 이동
        for i in range(len(cells)):
            # 이동
            cells[i][0] += dt[cells[i][3]][0]
            cells[i][1] += dt[cells[i][3]][1]

        # 2. 약품 셀에 도달했다면,
        # 미생물 // 2, 방향 반대방향으로 전환
        for i in range(len(cells)-1, -1, -1):
            cx, cy = cells[i][0], cells[i][1]
            if cx == 0 or cx == N-1 or cy == 0 or cy == N-1:
                # 미생물 수 줄이기
                cells[i][2] //= 2
                # 0이 되면 없애기
                if cells[i][2] == 0:
                    cells.pop(i)
                else:
                    # 방향 전환
                    c_dr = cells[i][3]
                    if c_dr % 2 == 0:
                        # 0, 2
                        cells[i][3] += 1
                    elif c_dr % 2 == 1:
                        # 1, 3
                        cells[i][3] -= 1

        # 3. 중복되는 좌표들의 세포 합치기
        for i in range(len(cells)):
            sm = 0
            pop_lst = []
            for j in range(len(cells)-1, i, -1):
                if cells[i][:2] == cells[j][:2]:
                    # 뒤에 있는 군집이 더 크면 -> 현재 군집의 방향을 그 방향으로 바꿔주기
                    if cells[i][2] < cells[j][2]:
                        cells[i][3] = cells[j][3]
                    # 군집 더하기
                    sm += cells[j][2]
                    # 뒤에 있는 군집 없애기
                    pop_lst.append(j)
            cells[i][2] += sm
            for p in pop_lst:
                cells.pop(p)

    ans = 0
    # 남은 미생물 수 더하기
    for cell in cells:
        ans += cell[2]

    print(f'#{tc} {ans}')