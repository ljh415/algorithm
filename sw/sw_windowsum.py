t = int(input())

for x in range(t) :
    # 최소값, 최대값 초기화
    min_value, max_value = 9999999999999999 , 0
    # 입력값
    n, m = list(map(int, input().split()))
    num_lst = list(map(int, input().split()))

    # 시작점을 지정해주고 0에서부터 뒤에서 3번째까지 시작점 순회
    for start_index in range(len(num_lst) - m +1) :
        # 시작점부터 시작점 + m의 위치까지 합을 tmp_lst에 저장
        check_num = sum(num_lst[start_index:start_index+m])

        if check_num > max_value :
            max_value = check_num

        if check_num < min_value :
            min_value = check_num

    print("#{} {}".format(x+1, max_value-min_value))