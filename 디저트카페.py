from collections import deque

dt = ((1, 1), (1, -1), (-1, 1), (-1, -1))
def bfs(sx, sy):
    # 큐 생성
    q = deque()
    # 큐에 시작점 넣기
    q.append((sx, sy))
    # 방문 배열 만들기
    visited = [[False] * N for _ in range(N)]
    # 시작점 방문처리
    visited[sx][sy] = True

    # 탐색 시작
    while q:
        # 현재 좌표 빼기



T = int(input())

for tc in range(1, T+1):
    # NxN 크기의 카페
    N = int(input())
    # 카페
    cafe = [list(map(int, input().split())) for _ in range(N)]

    # 탐색
    for i in range(N):
        for j in range(N):
            bfs(i, j)