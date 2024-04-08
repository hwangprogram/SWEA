'''
전략:
이용계획 리스트를 방문 배열로 사용한다.
dfs로 1일권, 1달권, 3달권, 1년권 사용하는 경우를 구분한다.
그 중 최소값을 찾는다.
'''

def dfs(cnt, cost):
    global min_cost

    # 기저조건: 12월까지 진행하고 종료
    if cnt == 12:
        # 정답처리: 최소값 구하기
        min_cost = min(min_cost, cost)
        return

    # 재귀조건: 각 이용권 사용하는 경우의 수
    # 1일권
    dfs(cnt + 1, cost + d * plan[cnt])
    # 1달권
    dfs(cnt + 1, cost + m)
    # 3달권: 10월까지만 사용가능
    if cnt < 10:
        dfs(cnt + 3, cost + m_3)
    # 1년권: 1월에만 사용가능
    if cnt == 0:
        dfs(cnt + 12, cost + y)


T = int(input())

for tc in range(1, T+1):
    # 1일, 1달, 3달, 1년 이용권 요금
    d, m, m_3, y = map(int, input().split())
    # 이용계획
    plan = list(map(int, input().split()))
    # 최소비용
    min_cost = float('inf')
    dfs(0, 0)
    print(f'#{tc} {min_cost}')