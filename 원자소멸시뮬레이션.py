'''
전략:
1. 한 칸 이동
2. 같은 좌표 -> 중복 표시
3. 중복 -> 삭제 (ans 누적)
   ㄴ 범위 밖 -> 삭제 (ans 누적 x)
0.5초 단위로 만나는 것도 있기 때문에 총 좌표 x2한다.
'''

# 방향 di, dj - 상, 하, 좌, 우
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T+1):
    # 원자들의 수 N
    N = int(input())
    # 원자들 목록 atoms
    atoms = [list(map(int, input().split())) for _ in range(N)]

    # 각 원자들의 좌표값 x2
    for i in range(len(atoms)):
        atoms[i][0] *= 2
        atoms[i][1] *= 2

    # 저장할 에너지 값
    energy = 0

    # 4000초동안 돌기 - 최대값
    for _ in range(4001):
        # 1. 각 좌표 이동
        for i in range(len(atoms)):
            atoms[i][0] += dj[atoms[i][2]]
            atoms[i][1] += di[atoms[i][2]]

        # 2. 중복되는 좌표 표시
        # 중복좌표 확인용
        V, ddel = set(), set()
        # 중복 확인 - 중복이면 삭제셋에 추가
        for i in range(len(atoms)):
            cj, ci = atoms[i][0], atoms[i][1]
            if (cj, ci) in V:
                ddel.add((cj, ci))
            else:
                V.add((cj, ci))

        # 3. 중복, 범위 밖 -> 삭제
        for i in range(len(atoms)-1, -1, -1):
            # 중복 (마지막부터 -> 인덱스값 유지를 위해)
            if (atoms[i][0], atoms[i][1]) in ddel:
                # 에너지 더해주기
                energy += atoms[i][3]
                # pop
                atoms.pop(i)
            # 범위 바깥:
            elif abs(atoms[i][0]) > 2000 or abs(atoms[i][1]) > 2000:
                atoms.pop(i)

    print(f'#{tc} {energy}')