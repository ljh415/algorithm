def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]

    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            # 방문을 한 적이 없다면 방문을 한것으로 처리
            if visited[j] == 0:
                visited[j] = 1
            # 그리고 computers 리스트를 순회하면서
            for i in range(0, len(computers)):
                # j는 현재 탐색하는 컴퓨터
                # i는 0부터 전체 컴퓨터를 다 비교를 하면서 j번 컴퓨터와 연결이 되어 있고,
                # 방문한 적이 없다면 그 컴퓨터를 스택에 넣는다.
                # dfs에서 현재 노드를 기준으로 연결되어 있는 노드들(중 방문을 한 적이 없는 노드)을 스택에 저장하는 것
                if computers[j][i] == 1 and visited[i] == 0:
                    stack.append(i)

    i = 0
    while 0 in visited:
        # 위에서 dfs를 돌면서 방문을 했다면 visited 리스트 또한 채워질 것
        # 여기서 방문을 한적이 없는 경우에만 dfs를 수행하도록 했다.
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1
    return answer

if __name__ == '__main__':
    n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    # n, computers = 3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    print(solution(n, computers))