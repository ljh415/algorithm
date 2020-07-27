# 버스가 0번에서 출발하고 N번 정류장까지 이동
# 한번 충전으로 이동할 수 있는 정류장 수 k가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때
# 최소한 몇번의 충전으로 종점에 도착하는가

import copy

iter_num = int(input())



for n in range(iter_num):
    answer = 0
    # K : 이동 가능한 정류장 수
    # N : 목적지 정류장
    # M : 충전소
    K, N, M = map(int, input().split(' '))    # 3 10 5

    # 입력 받은 이동 가능한 거리를 deepcopy를 사용해서 origin_K에 저장
    origin_K = copy.deepcopy(K)

    # 충전소 위치를 받아서 리스트에 저장
    station = list(map(int, input().split(' ')))  # 1 3 5 7 9
    # 목적지도 충전소 리스트 맨뒤에 추가해준다.
    station.append(N)

    for current in range(1, N):  # 한 정류장씩 이동
        # 정류장이 지날때마다 이동 가능한 정류장 하나 감소
        K -= 1

        # 도착지점과 현재 위치를 비교해서 남아있는 이동 가능한 거리보다 작을 경우 바로 반복문 탈출
        if N - current < K:
            break
        # 2번째 경우와 같이 종점에 도착하지 못할 경우
        elif K < 0 :
            answer = 0
            break
        # 충전소에 도착할때 마다 다음 충전소의 위치를 next_station에 저장
        # 다음 충전소의 위치와 현재 위치를 빼고 남은 이동 가능 거리를 비교해서
        # 다음 충전소까지 도착하지 못한다면 현재 충전소에서 충전을 하고
        # 이동 가능한 정류장 수를 초기화시켜준다.
        elif current in station :
            next_station = station[station.index(current):][1]
            if next_station - current > K :
                answer += 1
                K = origin_K

    print("#{} {}".format(n+1, answer))