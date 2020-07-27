'''import sys

N, R, C = map(int, input().split(' '))

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]
b = []


def solve(n, r, c, a) :
    if n == 2:
        for i in range(4) :
            if (r+dx[i], c+dy[i]) == (R, C) :
                b.append(a)
                print(sum(b))
                sys.exit(1)
            else :
                a += 1
        return b.append(a)

    solve(int(n/2), r, c, a)
    solve(int(n/2), r, c+int(n/2), a)
    solve(int(n/2), r+int(n/2), c, a)
    solve(int(n/2), r+int(n/2), c+int(n/2), a)

solve(pow(2, N), 0, 0, 0)'''

def div(row_start, row_end, col_start, col_end, num) :
    if r == row_start and c == col_start :
        print(num)
        return

    row_mid = (row_start + row_end) // 2
    col_mid = (col_start + col_end) // 2

    n = (row_mid - row_start) * (col_mid - col_start)
    #이게 뭐지

    if row_start <= r < row_mid and col_start <= c < col_mid :
        div(row_start, row_mid, col_start, col_mid, num)
    elif row_start <= r < row_mid and col_mid <= c < col_end :
        div(row_start, row_mid, col_mid, col_end, num+n)
    elif row_mid <= r < row_end and col_start <= c < col_mid :
        div(row_mid, row_end, col_start, col_mid, num+n*2)
    elif row_mid <= r < row_end and col_mid <= c < col_end :
        div(row_mid, row_end, col_mid, col_end, num+n*3)

N, r, c = map(int, input().split())
pow_ = 1 << N
#이부분도 모르겠다
div(0, pow_, 0, pow_, 0)