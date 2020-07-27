'''import numpy as np

N, M = map(int, input().split(' '))
matrix = []
paint = 0
start_x_index = 0
start_B = ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']
start_W = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']

for _ in range(N) :
    matrix.append(list(input()))

if matrix[0][0] == 'W' :
    for x in range(N) :
        if x%2 == 0 and matrix[x] != start_W :
            for y in range(M) :
                if matrix[x][y] != start_W[y] :
                    paint += 1
        elif x%2 == 1 and matrix[x] != start_B
else : # 시작이 'B'라면
    for x in range(N) :
        if matrix[x] != start_B :
            for y in range(M) :
                if matrix[x][y] != start_B[W] :
                    paint += 1


print(np.array(matrix))
print(paint)
# 모르겠다아아아아아

'''

N, M = map(int, input().split())
map_list = [list(input()) for _ in range(N)]

min_num = None

for i in range(N - 7):
    for j in range(M - 7):
        num1, num2 = 0, 0
        # W
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k + l - i - j) % 2 == 0):
                    if (map_list[k][l] == 'B'):
                        num1 += 1
                else:
                    if (map_list[k][l] == 'W'):
                        num1 += 1

        # B
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k + l - i - j) % 2 == 0):
                    if (map_list[k][l] == 'W'):
                        num2 += 1
                else:
                    if (map_list[k][l] == 'B'):
                        num2 += 1

        change_box = num1 if num1 < num2 else num2
        if (min_num is None):
            min_num = change_box
        else:
            min_num = change_box if min_num > change_box else min_num

print(min_num)

# 출처 : https://hwiyong.tistory.com/230