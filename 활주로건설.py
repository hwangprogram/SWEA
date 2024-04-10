def make_route(lst):
    global total

    for i in range(0, N):
        cnt = 1
        for j in range(1, N):
            # 앞, 뒤 같다면
            if lst[i][j] == lst[i][j-1]:
                cnt += 1
            # 낮 -> 높
            elif lst[i][j] - lst[i][j-1] == 1 and cnt >= X:
                cnt = 1
            # 높 -> 낮
            elif lst[i][j-1] - lst[i][j] == 1 and cnt >= 0:
                cnt = -X + 1
            else:
                break
        # for문을 다 돌았다면:
        else:
            # cnt가 0보다 크거나 같다면(범위를 벗어나지 않았다면)
            if cnt >= 0:
                total += 1


T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]
    rev_heights = list(zip(*heights))

    # 총 활주로 갯수
    total = 0
    make_route(heights)
    make_route(rev_heights)

    print(f"#{tc} {total}")