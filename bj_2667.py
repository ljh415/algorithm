'''import numpy as np
from collections import deque


# 0 : 오른쪽, 1 : 왼쪽, 2 : 위, 3 : 아래
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N = int(input())
dd = 1

matrix = [[0] * N for _ in range(N)]
for i in range(N) :
    a = list(input())
    matrix[i] = list(map(int, a))

check = [[False] * N for _ in range(N)]
danji = [[0] * N for _ in range(N)]

q = deque()  # 현재의 위치를 나타낼때
temp = deque()

# 시작점
q.append((0,0))
check[0][0] = True

while q :
    x, y = q.popleft()
    if matrix[x][y] == 1 and check[x][y] == False :   # (0, 0)부터 집이 있을 경우
        danji[x][y] = dd
        check[x][y] = True
    else :
        nx, ny = x+dx[0], y+dy[0]   # 먼저 오른쪽으로 탐색
        if 0 <= nx < N and 0 <= ny < N :    # index가 넘어가는 것을 확인하기 위해서
            if matrix[nx][ny] == 1 and check[nx][ny] == False :  # 집, 방문처리 확인
                q.append((nx, ny))
                temp.append((nx,ny))  # 위치 임시저장
                danji[nx][ny] = dd
                check[nx][ny] = True

                for k in range(4) :
                    nx, ny







        if check[nx][ny] == False and matrix[nx][ny] == 1 :
            q.append((nx, ny))
            danji[nx][ny] = dd
            check[nx][ny] = True

            for k in range(4) :
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < N :
                    q.append((nx, ))


matrix_np = np.array(matrix)
check_np = np.array(check)
print(matrix_np)
print(check_np)
'''

import sys
read = lambda : sys.stdin.readline().strip()

n = int(read())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(matrix, cnt, x, y):
    matrix[x][y]=0
    # 이건 이제 이미 간것이다. 그래서 0으로 바꾼다
    queue = []
    queue.append((x, y))
    while len(queue) > 0:
        x, y = queue.pop()
        for k in range(0, 4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx and nx< n and 0<= ny and ny <n:
                if matrix[nx][ny] == 1:
                    cnt += 1
                    matrix[nx][ny] = 0
                    queue.append((nx, ny))
    return cnt

matrix = [list(map(int, list(read()))) for _ in range(n)]
# matrix에 input값 넣기

cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            # 일단 1로 뭔가의 그룹이다.
            ans.append(bfs(matrix, cnt+1, i, j))
            # 여기서 이제 그 주위에 있는 것들 다 돌아보는것이다.
print(len(ans))
for i in sorted(ans):
    print(i)