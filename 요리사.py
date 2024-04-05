# def flavor_diff(arr1, arr2):


def make_team(cnt):
    global food_1, food_2

    # 기저조건: 재료가 N//2가 되면 되면 종료
    if len(food_1) == N//2:
        # 음식 2 만들기
        food_2 = list(set(all_mat) - set(food_1))
        # 두 음식간 시너지 차이 계산하기
        flavor_diff(food_1, food_2)
        return

    # 재귀조건: 재료를 넣느냐, 마느냐
    for i in range(cnt, N):
        # 중복 제거
        if len(food_1) > 0 and food_1[-1] == i:
            continue
        food_1.append(i)
        make_team(i+1)
        food_1.pop()


T = int(input())

for tc in range(1, T+1):
    # 재료 갯수 N
    N = int(input())
    # 모든 재료 배열
    all_mat = list(range(N))
    # 시너지들 synerges
    synerges = [list(map(int, input().split())) for _ in range(N)]

    # 음식 1, 음식 2
    food_1 = []
    food_2 = []
    # 팀 만들기 시작 (DFS)
    make_team(0)