def MST_PRIM(G):
    key = [float('inf') for _ in range(V+1)]
    pi = [None for _ in range(V+1)]
    visited = [False for _ in range(V+1)]

    key[0] = 0
    for _ in range(V+1):
        # 최소 key (start지점)찾기
        min_key = float('inf')
        start = -1
        for i in range(V+1):
            if key[i] < min_key and not visited[i]:
                min_key = key[i]
                start = i
        # 방문 & 주변 key값 갱신
        visited[start] = True
        for next_v, next_w in G[start] :
            if next_w < key[next_v] and not visited[next_v]:
                key[next_v] = next_w
                pi[next_v] = start
    return sum(key)

T = int(input())
for test_case in range(1, 1+T) :
    V, E = map(int, input().split())
    my_graph = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        if n1 not in my_graph:
            my_graph[n1] = set()
        if n2 not in my_graph:
            my_graph[n2] = set()
        my_graph[n1].add((n2, w))
        my_graph[n2].add((n1, w))
    print(f'#{test_case} {MST_PRIM(my_graph)}')