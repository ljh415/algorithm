from collections import defaultdict, deque

def make_graph(connection) :

    graph = defaultdict(int)

    for i in range(connection) :
        a, b = map(int, input().split(' '))

        if graph[a] :
            tmp = graph[a]
            tmp.append(b)
            graph[a] = tmp
        else :
            graph[a] = [b]

        if graph[b] :
            tmp = graph[b]
            tmp.append(a)
            graph[b] = tmp
        else:
            graph[b] = [a]

    return graph

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue :
        v = queue.popleft()
        # print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v] :
            if not visited[i]:
                queue.append(i)
                visited[i] = True



computer = int(input())
connection = int(input())

visited = [False] * (computer+1)
graph = make_graph(connection)

bfs(graph, 1, visited)
visited = visited[1:]

answer = 0
for k in visited :
    if k :
        answer += 1
print(answer-1)
# print(visited)