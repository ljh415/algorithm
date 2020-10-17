def Dijkstra(my_map):
    key = [[float('inf')] * N for _ in range(N)]  # 연료 사용량
    confirm = [[False] * N for _ in range(N)]  # key값 확정 여부
    key[0][0] = 0
    check = set()  # 탐색 할 범위
    check.add((0, 0))
    while True:
        # 최소 key 찾기
        min_key = float('inf')
        for r, c in check:
            if key[r][c] < min_key and not confirm[r][c]:
                min_key = key[r][c]
                y, x = r, c

        # 최소 key 확정
        confirm[y][x] = True
        check.remove((y, x))
        # 도착지점이면
        if y == x == N - 1:
            return key[y][x]

        # 다음 지점 찾기
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not confirm[ny][nx]:
                # 연료 계산
                if my_map[y][x] < my_map[ny][nx]:
                    fuel = key[y][x] + my_map[ny][nx] - my_map[y][x] + 1
                else:
                    fuel = key[y][x] + 1
                # key 갱신
                if fuel < key[ny][nx]:
                    key[ny][nx] = fuel
                    check.add((ny, nx))


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    my_map = [list(map(int, input().split())) for _ in range(N)]
    # right down left up
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    print('#{} {}'.format(test_case, Dijkstra(my_map)))