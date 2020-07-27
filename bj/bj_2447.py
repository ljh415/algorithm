'''import numpy as np
import math

N = int(input())
arr = [['*']*N]*N
arr = np.array(arr)

def star(n, x, y) :

    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if (i >= x+int(math.log(n, 3)) and i < x+int(math.log(n*3, 3))) and \
                    (j >= y+int(math.log(n, 3)) and j < y+int(math.log(n*3, 3))) :
                arr[i, j] = ' '


    for h in range(int(n/3)) :
        for g in range(int(n/3)) :
            star(int(n/3), x+h*3, y+g*3)

star(N, 0, 0)
print(arr)'''


# dp? 모양을 보니 반복되는 모양이 있다.
# 입력값도 3의 제곱꼴이고, 가운데가 비어있는 사각형모양으로 출력..


def stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return (list(matrix))


star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    star = stars(star)

for i in star:
    print(i)

# 출처 : https://claude-u.tistory.com/146