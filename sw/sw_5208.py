def solution_a():
    T = int(input())

    for t in range(T):
        tmp_lst = input().split()
        N, battery = int(tmp_lst[0]), list(map(int, tmp_lst[1:]))+[0]
        print(N, battery)
        remain, answer = 0, 0
        # 일단 정류장을 순회
        for n in range(len(battery)) :
            if remain >= N+1-n :
                print(f'remain : {remain}, answer : {answer}')
                break

            if n == 0 :
                remain += battery[n]
            else :
                remain -= 1

                if battery.index(max(battery[n:])) == n :
                    remain += battery[n]
                    answer += 1
                    continue

                if remain < n+1-tt:
                    remain += battery[n]
                    answer += 1
                elif remain > 0 :
                    continue
                else :
                    remain += battery[n]
                    answer+=1

##
def solution_b():
    T = int(input())
    for test_case in range(1, 1+T):
        N, *M = map(int, input().split())

        # 초기값
        bus = 0
        bus_battery = M[bus]
        cnt = 0

        while bus + bus_battery < N - 1:
            max_charge = 0
            next_bus = None
            for i in range(bus_battery, 0, -1):  # 갈 수 있는 충전소 중
                charge = M[bus + i] - (bus_battery-i)  # 충전가능한 양
                if charge > max_charge:  # 최대값을 찾아서
                    max_charge = charge
                    next_bus = bus + i
            if next_bus is None:
                cnt = -1
            else:
                bus = next_bus
                bus_battery = M[bus]
                cnt += 1

        print(f'#{test_case} {cnt}')

if __name__ == '__main__':
    solution_b()