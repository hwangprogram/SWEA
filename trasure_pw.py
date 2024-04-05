T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = input()

    pw_lst = []      # 패스워드 리스트
    for i in range(N // 4):
        for j in range(0, N, N // 4):
            pw_lst.append(num[j:j + N // 4])
        rot = num[0]
        num = num[1:] + rot
    pw_lst = list(set(pw_lst))

    for i in range(len(pw_lst)):   # 16진수 -> 10진수 변환
        pw_lst[i] = int(pw_lst[i], 16)

    pw_lst.sort(reverse=True)

    print(f'#{tc} {pw_lst[K-1]}')