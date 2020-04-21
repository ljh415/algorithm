def solution(triangle):
    answer = 0

    root, left, right = 0, 0, 0
    tmp = 0

    for i in range(len(triangle)-1) :
        for j in range(len(triangle[i])) :
            # i, j는 시작하는 점의 index를 표현함
            # 왼쪽 자식노드를 계산할 때 j=0에서는 그대로 더해서 채우고
            # j가 0이 아닐 경우에는 오른쪽 노드를 맨처음에 tmp에 담고
            # 다음 i, j연산을 시작할 때 왼쪽노드 계산시에 tmp와 비교후 왼쪽노드를 바꿔주고
            # 오른쪽 노드는 다시 tmp에
            # j가 마지막을 탐색할때 오른쪽 자식노드는 j = 0일때 처럼 오른쪽에 그대로 채워줌
            root = triangle[i][j]
            left = triangle[i+1][j]
            right = triangle[i+1][j+1]
            if i == 0 and j == 0 :
                triangle[i+1][j] = root + left
                triangle[i+1][j+1] = root + right
                continue

            if j == 0 :
                triangle[i+1][j] = root + left
                tmp = root + right
            else :
                # j == 1부터 왼쪽노드 계산
                if tmp < root + left :
                    triangle[i+1][j] = root + left
                else :
                    triangle[i+1][j] = tmp

                if j == len(triangle[i])-1 :
                    triangle[i+1][j+1] = root+right
                else :
                    tmp = root + right

    # print(triangle)

    return max(triangle[len(triangle)-1])

if __name__ == '__main__':
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    print(solution(triangle))