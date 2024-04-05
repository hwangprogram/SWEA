'''
문제에서 잘 파악해야 하는 문제의 의도
예를들어 단어의 길이가 3이라면, 반드시 길이가 3인 빈칸에만 들어갈 수 있다
즉, 단어의 길이만큼 있는 빈칸의 갯수를 세는 문제이다.
'''

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())    # 퍼즐의 가로세로길이 N, 단어의 길이 K

    puzzle = [list(map(int, input().split())) for _ in range(N)]    # 퍼즐 모양

    cnt_lst = []     # 단어의 길이와 맞는 빈칸 갯수

    # 가로 순회하며 길이가 K인 빈칸찾기
    for i in range(N):
        cnt = 0  # 퍼즐의 빈칸을 세어줄 변수 cnt
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
                if j == N-1:        # 끝에 도달했을 때
                    cnt_lst.append(cnt)
                    cnt = 0
            elif cnt > 0 and puzzle[i][j] == 0:  # 카운트 세는 도중 0을 만났을 때
                cnt_lst.append(cnt)
                cnt = 0

    # 배열 90도 회전
    rev_pzl = [list(tp) for tp in zip(*puzzle)]

    for i in range(N):  # 똑같이 세어주기
        cnt = 0  # 퍼즐의 빈칸을 세어줄 변수 cnt
        for j in range(N):
            if rev_pzl[i][j] == 1:
                cnt += 1
                if j == N - 1:      # 끝에 도달했을 때
                    cnt_lst.append(cnt)
                    cnt = 0
            elif cnt > 0 and rev_pzl[i][j] == 0:  # 카운트 세는 도중 0을 만났을 때
                cnt_lst.append(cnt)
                cnt = 0

    print(f'#{tc} {cnt_lst.count(K)}')
