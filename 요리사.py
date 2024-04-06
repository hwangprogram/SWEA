# 팀 1, 팀 2
team1 = []
# 팀 뽑기: (N/2)명
def dfs(st, n):
    # 차이 최소값
    global mn_dif

    # 기저조건 : cnt가 N/2 이상 되면 종료
    if len(team1) == N//2:
        # 정답처리 : team2에 team1을 제외한 사람들 넣기, 각 팀 별 가치 계산
        # team2 생성
        team2 = list(set(range(1, N+1)) - set(team1))
        # 팀 별 가치 계산
        val1 = team_value(team1)
        val2 = team_value(team2)
        dif = abs(val1 - val2)
        # 최소값 갱신
        mn_dif = min(dif, mn_dif)
        return

    # 재귀조건 : 팀에 멤버를 추가하는 경우, 하지않는 경우
    for i in range(st, n+1):
        # 같은 멤버 x, 중복되는 경우 제거
        if i not in team1:
            team1.append(i)
            dfs(i+1, n)
            team1.pop()


# 팀 가치 계산 함수
def team_value(team):
    # 합
    val = 0

    # 2개씩 뽑아서 더하기
    for i in range(len(team)):
        for j in range(i+1, len(team)):
            p1, p2 = team[i]-1, team[j]-1

            val += S[p1][p2] + S[p2][p1]

    return val


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    mn_dif = 2000
    dfs(1, N)
    print(f'#{tc} {mn_dif}')
