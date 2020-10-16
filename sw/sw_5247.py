from collections import deque

def bfs():
    global start_num, end_num, result, tc
    while Q:
        num, cnt = Q.popleft()
        if num == end_num:
            result = cnt
            return

        # +1, -1, *2 -10
        for i in range(4):
            num2 = 0
            if i == 0:
                num2 = num + 1
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 1:
                num2 = num - 1
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt+1))
                    num_lst[num2] = tc

            elif i == 2 :
                num2 = num * 2
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt + 1))
                    num_lst[num2] = tc

            elif i == 3:
                num2 = num - 10
                if 0 < num2 <= 1000000 and num_lst[num2] != tc:
                    Q.append((num2, cnt + 1))
                    num_lst[num2] = tc


TC = int(input())
num_lst = [0] * 1000001
for tc in range(1, TC+1) :
    start_num, end_num = map(int, input().split())
    Q = deque()
    Q.append((start_num, 0))
    num_lst[start_num] = tc
    result = 0
    bfs()
    print(f'#{tc} {result}')
