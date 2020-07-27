# 버스가 0번에서 출발하고 N번 정류장까지 이동
# 한번 충전으로 이동할 수 있는 정류장 수 k가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때
# 최소한 몇번의 충전으로 종점에 도착하는가

import copy

iter_num = int(input())



for n in range(iter_num):
    answer = 0

    K, N, M = map(int, input().split(' '))        # 3 10 5
    origin_K = copy.deepcopy(K)
    # 한번에 이동할 수 있는 정류장수 3개
    # 0~10까지 있는 정류장, 10번정류장 까지 이동
    # 충전소는 5개
    station = list(map(int, input().split(' ')))  # 1 3 5 7 9
    # 5개는 다음과 같이 1, 3, 5, 7, 9


    for current in range(1, N):  # 한칸씩 이동

        K -= 1
        # if K == -2 :
        #     print(n, 0)
        #     pass
        if N - current < K:
            break
        elif K < 0 :
            answer = 0
            break
        elif current in station :
            # try :
            next_station = station[station.index(current):][1]
            # except :
            #     print('ss')
                # if N - current < origin_K :
                #     answer+=1
                #     break
            if next_station - current > K :
                answer += 1
                K = origin_K
    print(n, answer)