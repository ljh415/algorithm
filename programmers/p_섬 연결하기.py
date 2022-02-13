def solution(n, costs):
    answer = 0
    visited = set()
    # 방문한 곳에 0을 저장
    visited.add(costs[0][0])
    costs = sorted(costs, key=lambda x : x[2])
    print(costs)

    while len(visited) != n :

        for cost in costs :
            land1, land2, co = cost
            if land1 in visited and land2 in visited :
                continue
            if land1 in visited or land2 in visited :
                answer += co
                visited.add(land1)
                visited.add(land2)
                break

    return answer

# 실패
def solution2(n, costs):
    answer = 0
    visited = set()

    costs = sorted(costs, key=lambda x : x[2])
    # print(costs)

    for cost in costs :
        land1, land2, co = cost
        if land1 not in visited or land2 not in visited :
            answer += co
            visited.add(land1)
            visited.add(land2)

        if len(visited) == n :
            print(visited)
            return answer


if __name__ == '__main__':
    n, costs = 4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
    # n, costs = 5, [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]
    # n, costs = 6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]

    print(solution(n, costs))