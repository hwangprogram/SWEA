from collections import deque

# 각 터널들의 델타값
dt = {
    1: ((1, 0, 'd'), (-1, 0, 'u'), (0, 1, 'r'), (0, -1, 'l')),
    2: ((1, 0, 'd'), (-1, 0, 'u')),
    3: ((0, 1, 'r'), (0, -1, 'l')),
    4: ((-1, 0, 'u'), (0, 1, 'r')),
    5: ((1, 0, 'd'), (0, 1, 'r')),
    6: ((1, 0, 'd'), (0, -1, 'l')),
    7: ((-1, 0, 'u'), (0, -1, 'l')),
}


# 가능한 통로 찾기
def is_possible_route(now_dir, next_dir_tp):
    # 위 방향이라면, 다음 통로애 아래가 반드시 포함
    if now_dir == 'u':
        for next_dir in next_dir_tp:
            if next_dir[-1] == 'd':
                return True
        else:
            return False
    # 아래 방향이라면, 다음 통로애 위가 반드시 포함
    elif now_dir == 'd':
        for next_dir in next_dir_tp:
            if next_dir[-1] == 'u':
                return True
        else:
            return False
    # 오른 방향이라면, 다음 통로애 왼쪽이 반드시 포함
    elif now_dir == 'r':
        for next_dir in next_dir_tp:
            if next_dir[-1] == 'l':
                return True
        else:
            return False
    # 왼 방향이라면, 다음 통로애 오른쪽이 반드시 포함
    elif now_dir == 'l':
        for next_dir in next_dir_tp:
            if next_dir[-1] == 'r':
                return True
        else:
            return False


def bfs(sx, sy):
    # 큐 만들기
    q = deque()
    # 방문 배열 만들기
    visited = [[False] * M for i in range(N)]
    # 큐에 시작점, 시간 넣기
    q.append((sx, sy, 1))
    # 시작점 방문 처리
    visited[sx][sy] = True

    # 카운트 (범인이 위치할 수 있는 방의 수)
    cnt = 0

    # 탐색 시작
    while q:
        # 시작점 뽑기
        x, y, time = q.popleft()

        # time이 L 이하인 것들만 카운트
        if time <= L:
            cnt += 1

        # 시작점의 터널 확인 (어떤 델타값으로 해야 할 지)
        for dx, dy, dr in dt[stage[x][y]]:
            # 다음 좌표값
            nx, ny = x + dx, y + dy
            # 범위 내라면
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았으며, 0이 아니며 (통로라면), 이어질 수 있는 통로라면
                if not visited[nx][ny] and stage[nx][ny] != 0 and is_possible_route(dr, dt[stage[nx][ny]]):
                    # 방문처리
                    visited[nx][ny] = True
                    # 큐에 넣기
                    q.append((nx, ny, time+1))
    return cnt


T = int(input())

for tc in range(1, T+1):
    # 지도 세로 크기 N, 가로 크기 M, 맨홀 뚜껑 좌표 R, C, 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    # 지도 정보 stage
    stage = [list(map(int, input().split())) for _ in range(N)]

    # 탐색
    print(f'#{tc} {bfs(R, C)}')