from collections import deque

dt = ((1, 1), (1, -1), (-1, 1), (-1, -1))
def bfs(sx, sy):
    global max_cnt

    # 큐 생성
    q = deque()
    # 큐에 시작점, 카운트 넣기
    q.append((sx, sy, 0))
    # 방문 배열 만들기
    visited = [[False] * N for _ in range(N)]
    # 시작점 방문처리
    visited[sx][sy] = True
    # 디저트들의 배열
    desserts = [cafe[sx][sy]]

    # 탐색 시작
    while q:
        # 현재 좌표, 카운트 빼기
        x, y, cnt = q.popleft()

        # 도착점: 시작점에 다시 도착했으며, 카운트가 0이 아니라면 종료
        if x == sx and y == sy and cnt != 0:
            # 지금까지의 cnt값 중 최대값 찾기
            max_cnt = max(max_cnt, len(desserts))
            # 다저트 배열 초기화
            desserts = [cafe[sx][sy]]

        # 다음 좌표 탐색
        for dx, dy in dt:
            nx, ny = x + dx, y + dy

            # 범위 내라면
            if 0 <= nx < N and 0 <= ny < N:
                # 방문하지 않은 곳이며, 디저트 배열 내에 없는 디저트라면,
                if not visited[nx][ny] and (cafe[nx][ny] not in desserts):
                    # 방문처리
                    visited[nx][ny] = True
                    # 큐에 추가
                    q.append((nx, ny, cnt+1))
                    # 디저트 배열에 추가
                    desserts.append(cafe[nx][ny])
                # 시작점이라면
                if nx == sx and ny == sy:
                    # 큐에 추가 (카운트 세지 않고
                    q.append((nx, ny, cnt))


T = int(input())

for tc in range(1, T+1):
    # NxN 크기의 카페
    N = int(input())
    # 카페
    cafe = [list(map(int, input().split())) for _ in range(N)]

    # 탐색
    # 마지막 루트 길이
    final_route_len = -1
    # 각 좌표별 최대 길이
    max_cnt = -1
    for i in range(N):
        for j in range(N):
            # 좌표별 최대 길이 초기화
            max_cnt = -1
            bfs(i, j)
            # 마지막 루트에 최댓값 넣기
            final_route_len = max(max_cnt, final_route_len)

    print(f'#{tc} {final_route_len}')