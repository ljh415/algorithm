T = int(input())

def search(matrix, n) :

    for i in range(1, n+1):
        matrix[0][i] += matrix[0][i-1]
        matrix[i][0] += matrix[i-1][0]

    for i in range(1, n+1):
        for j in range(1, n+1):
            matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])

    return matrix[n][n]

for t in range(T) :
    matrix = []
    N = int(input())
    for n in range(N) :
        row = list(map(int, input().split()))
        matrix.append(row)

    print(f'#{t+1} {search(matrix, n)}')