T = int(input())

for t in range(T):
    tmp_lst = input().split()
    N, battery = int(tmp_lst[0]), list(map(int, tmp_lst[1:]))
    print(N, battery)

    answer, remain, result = -1, 0, 9999
    for i in range(N) :
        # 0, 1, 2, 3, 4
        if remain < (N-i+1):
            remain += battery[i]
            answer += 1
        else :
            if result > answer :
                result = answer
            else :
                continue

    print(f'#{t+1} {result}')