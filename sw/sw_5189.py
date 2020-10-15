from itertools import permutations

T = int(input())

for t in range(T) :
    matrix = []
    N = int(input())

    route = list(range(N))[1:]
    route = list(permutations(route))

    for n in range(N) :
        row = list(map(int, input().split()))
        matrix.append(row)

    answer_list = []

    for r in route:
        answer = 0
        for i in range(len(r)):
            if i == 0:
                answer += matrix[0][r[i]]
            else :
                answer += matrix[r[i-1]][r[i]]

        answer += matrix[r[i]][0]
        answer_list.append(answer)

    print(f'#{t+1} {min(answer_list)}')