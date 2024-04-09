from collections import deque

# 2. 벽돌 부수기
dt = ((1, 0), (-1, 0), (0, 1), (0, -1))
def break_bricks(sx, sy):
    '''
    :param bizs: 구슬 위치 배열
    로직:
    bfs를 진행하며, 그 때, 자기 자신이 가지고 있는 value값도 같이 가지고 간다.
    값을 꺼내서 확인할 때마다, value값만큼 이동하며 전부 큐에 집어넣는다.
    '''
    # 큐 생성
    q = deque()
    # 시작점, 시작점의 value 큐애 넣기
    q.append((sx, sy, bricks[sx][sy]))
    # 시작점 방문처리 (0으로 만들기)
    bricks[sx][sy] = 0

    # 탐색 시작
    while q:
        # 현재 좌표, value뽑아서 확인
        x, y, val = q.popleft()

        for dx, dy in dt:
            # 0부터 해도 상관 x -> 이미 자신은 방문처리 했기 때문
            for k in range(val):
                nx, ny = x + dx * k, y + dy * k

                # 범위 내인지 확인
                if 0 <= nx < H and 0 <= ny < W:
                    # 다음 좌표가 0이 아니면 q에 추가
                    if bricks[nx][ny] != 0:
                        q.append((nx, ny, bricks[nx][ny]))
                        # 방문처리
                        bricks[nx][ny] = 0

# 3. 정렬하기
def sorting():
    '''
    로직:
    배열의 아래서부터 순회하며 0이 나오면, 위에 0이 아닌 값이 있으면 위치 교체
    '''
    for j in range(W):
        for i in range(H-1, -1, -1):
            # 0 이 나오면
            if bricks[i][j] == 0:
                # 위에 0이 아닌값 찾아가기
                for k in range(i, -1, -1):
                    # 0이 아닌값 찾았다면
                    if bricks[k][j] != 0:
                        # 값 변경
                        bricks[i][j], bricks[k][j] = bricks[k][j], bricks[i][j]
                        break


# 시작점 찾기
def find(point):
    # point열에서 내려가며 0이 아닌 값 찾기
    for i in range(H):
        if bricks[i][point] != 0:
            return i, point
    return None, None


# 1. 구슬 위치, 순서 뽑기
def order():
    global biz, bricks, min_bizs

    # 기저조건 : biz 길이가 N이되면 종료
    if len(biz) == N:
        # 초기화
        bricks = [row[:] for row in og_bricks]
        for b in biz:
            # 시작점 찾기
            st_x, st_y = find(b)
            if st_x is not None and st_y is not None:
                # 부수기
                break_bricks(st_x, st_y)
                # 정렬하기
                sorting()
        # 남은 벽돌 갯수 세기
        biz_cnt = 0
        for i in range(H):
            for j in range(W):
                if bricks[i][j] != 0:
                    biz_cnt += 1
        # 최소값 갱신
        min_bizs = min(biz_cnt, min_bizs)
        return

    # 재귀조건 : 0~W-1 중에서 고르기 - 추가하거나, 하지않거나
    for i in range(W):
        biz.append(i)
        order()
        biz.pop()


T = int(input())

for tc in range(1, T+1):
    # N개의 구슬, 가로길이 W, 세로길이 H
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    og_bricks = [row[:] for row in bricks]

    # 구슬 순서 뽑기
    biz = []
    # 남은 구슬 최소값
    min_bizs = float('inf')
    order()

    print(f'#{tc} {min_bizs}')