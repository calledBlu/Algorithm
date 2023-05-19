# 우 하 좌 상 방향 설정
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

# 초기 r, c, 방향값 설정

T = int(input()) # 테스트 케이스의 개수 받기

for tc in range(1, T+1):
    r = c = d = 0
    N = int(input())
    # n*n 짜리 인접행렬 생성하기
    adj_list = [[0]*N for _ in range(N)]
    # 숫자 넣기 시작, N**2개만큼 넣어야 하니까 N**2번 반복하도록
    for num in range(1, N**2+1):
    # 일단 숫자를 하나 넣어주고
        adj_list[r][c] = num
    # 좌표를 이동해줌(정해진 방향으로)
        nr = r + dr[d]
        nc = c + dc[d]
    # 이동한 후의 좌표가 (0보다 작거나) or (N보다 크거나) or (새 좌표의 자리 숫자가 0이 아닌 경우)
        if 0 > nr or nr >= N or 0 > nc or nc >= N or adj_list[nr][nc] != 0:
    # 방향 변경
        # 0-1-2-3
        # (d+1) % 4
            d = (d+1) % 4
            nr, nc = r+dr[d], c+dc[d]
    # 새 좌표 설정
        r = nr
        c = nc

    print(f'#{tc}')
    for ans in adj_list:
        print(*ans)
    # 이번 문제는 개행하고 출력됨!