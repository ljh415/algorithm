answer = 0

def dfs(begin, target, words, visited) :
    global answer
    stacks = [begin]

    while stacks :
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()

        if stack == target:
            return answer

        for w in range(len(words)):
            if len([i for i in range(len(words[w])) if words[w][i] != stack[i]]) == 1:

                if visited[w] != 0:
                    continue

                visited[w] = 1

                # stack에 추가
                stacks.append(words[w])
        # depth +
        answer += 1

def solution(begin, target, words):
    global answer

    # 조건 2. words에 있는 단어로만 변경 가능
    if target not in words :
        return 0

    visited = [0 for i in words]

    dfs(begin, target, words, visited)

    return answer


### 진짜 좋은 풀이
# https://cocojelly.github.io/algorithm/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%97%B0%EC%8A%B5-DFS-BFS-(3)/

from collections import deque as queue

transistable = lambda a,b: sum((1 if x != y else 0) for x,y in zip(a,b)) == 1

def solution_2(begin, target, words):
    q, d = queue(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x:transistable(x,begin), words))

    for w in words :
        d[w] = set(filter(lambda x: transistable(x, w), words))

    while q:
        cur, level = q.popleft()
        if level > len(words):
            return 0
        for w in d[cur]:
            if w == target:
                return level + 1
            else:
                q.append((w, level+1))
    return 0

if __name__ == '__main__':
    begin, target, words = 'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    # begin, target, words = 'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']

    print(solution_2(begin, target, words))