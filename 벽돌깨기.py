def make_subsets():
    global mn_remain, bricks

    # 기저조건 : combinations의 길이가 N이 되면 종료
    if len(combinations) == N:
        # 정답처리 : 변환 다 돈다음 남은것들 계산
        for n in combinations:
            brick_find(n)
        remain = 0
        for i in range(H):
            remain += sum(bricks[i])
        mn_remain = min(remain, mn_remain)
        # 초기화
        bricks = copy_bricks
        return

    # 재귀조건 : 0~W-1 사이 숫자 넣느냐 마느냐
    for w in range(W):
        combinations.append(w)
        make_subsets()
        combinations.pop()


# 벽돌 찾기
def brick_find(n):
    # 위에서 첫 번째 벽돌 찾기
    start = tuple()
    for h in range(H):
        if bricks[h][n] != 0:
            start = (h, n)
            break

    x, y = start[0], start[1]
    break_bricks(x, y)


# 벽돌깨기 (아래, 오, 왼)
dt = ((1, 0), (0, 1), (0, -1))


def break_bricks(x, y):
    # 탐색 1인경우, 1보다 큰 경우
    if bricks[x][y] == 1:
        # 방문처리 (연쇄반응 x)
        bricks[x][y] = 0
    else:
        # 그 값만큼 계속해서 연쇄
        val = bricks[x][y]
        # 방문처리
        bricks[x][y] = 0
        for dx, dy in dt:
            for v in range(val):
                nx, ny = x + dx * v, y + dy * v

                # 범위 내라면
                if 0 <= nx < H and 0 <= ny < W:
                    # 1이라면
                    if bricks[nx][ny] == 1:
                        # 방문처리
                        bricks[nx][ny] = 0
                    # 아니라면 > 재귀
                    else:
                        break_bricks(nx, ny)


T = int(input())

for tc in range(1, T + 1):
    # 공의 갯수 N, 열 W, 행 H
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    copy_bricks = bricks[:]

    # 최소 남은 벽돌
    mn_remain = float('inf')
    # W에서부터 N개의 조합 뽑기
    combinations = []
    make_subsets()
    print(mn_remain)