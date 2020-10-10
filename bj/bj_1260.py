from collections import defaultdict, deque

def make_graph(m) :
    graph = defaultdict(int)
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a]:
            tmp = graph[a]
            tmp.append(b)
            tmp = sorted(tmp)
            graph[a] = tmp
        else :
            graph[a] = [b]

        if graph[b] :
            tmp = graph[b]
            tmp.append(a)
            tmp = sorted(tmp)
            graph[b] = tmp
        else :
            graph[b] = [a]
    return graph

def DFS(graph, start, visited) :
    visited[start-1] = True
    print(start, end=' ')
    try:
        for i in graph[start]:
            if not visited[i-1]:
                DFS(graph, i, visited)
    except :
        pass

def BFS(graph, start, vistied):
    queue = deque([start])
    visited[start-1] = True
    # print(start, end=' ')
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        try :
            for i in graph[v]:
                if not vistied[i-1]:
                    queue.append(i)
                    visited[i-1] = True
                    # print(i, end=' ')
        except :
            pass

n, m, v = map(int, input().split())
visited = [False] * n

graph = make_graph(m)
DFS(graph, v, visited)

visited = [False] * n
print()
BFS(graph, v, visited)

## 예외의 경우 : 시작점에 연결된 간선이 없을 때 에러가 발생
# in:
# 1000 1 1
# 999 1000
# out :
# 1
# 1
