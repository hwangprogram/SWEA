'''
로직:
각 칸에 있는 숫자들은 카운트이다.
시작하면 이 숫자들이 줄어들기 시작한다.
0이 되었을 때, 자신이 가진 파워 시간만큼 퍼진다.
(이때 자신의 파워 값은 가지고 있어야 함 - 힘 비교하여 센 녀석이 번식되어야 하므로)
활성화, 비활성화 여부는 상관 X - 0이면 죽은 것이기 때문
각 세포들을 어떻게 지정해서 번식시킬 것인가?

'''

T = int(input())

for tc in range(1, T+1):
    # 세로크기 N, 가로크기 M, 배양시간 K
    N, M, K = map(int, input().split())
    # 생명력 lifetimes
    liftimes = [list(map(int, input().split())) for _ in range(N)]

