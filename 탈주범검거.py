from collections import deque

# 각 터널들의 델타값
# 1. 상, 하, 좌, 우
dt1 = ((1, 0), (-1, 0), (0, 1), (0, -1))
# 2. 상, 하
dt2 = ((1, 0), (-1, 0))
# 3. 좌, 우
dt3 = ((0, 1), (0, -1))
# 4. 상, 우
dt4 = ((-1, 0), (0, 1))
# 5. 하, 우
dt5 = ((1, 0), (0, 1))
# 6. 하, 좌
dt6 = ((1, 0), (0, -1))
# 7. 상, 좌
dt7 = ((-1, 0), (0, -1))

def bfs(sx, sy):
    # 큐 만들기
    q = deque()
    # 방문 배열 만들기
    visited = [[False] * M for i in range(N)]
    # 큐에 시작점 넣기
    q.append((sx, sy))
    # 시작점 방문 처리
    visited[sx][sy] = True

    # 탐색 시작
    while q:
        # 시작점 뽑기
        x, y = q.popleft()
        # 시작점의 터널 확인
        



T = int(input())

for tc in range(1, T+1):
    # 지도 세로 크기 N, 가로 크기 M, 맨홀 뚜껑 좌표 R, C, 탈출 후 소요된 시간 L
    N, M, R, C, L = map(int, input().split())
    # 지도 정보 stage
    stage = [list(map(int, input().split())) for _ in range(N)]

    # 탐색 시작
    bfs(R, C)