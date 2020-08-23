def solution(bridge_length, weight, truck_weights):
    answer = 0 #시간
    # 트럭저장하는 큐 (리스트로 만듬)
    t_list = []

    # 트럭뽑는 함수
    for i in truck_weights :
        q_truck = i
        while q_truck != 0 : # 트럭이 빠질 때까지 확인하기 위해서
            if len(t_list) == bridge_length : # t_list의 길이가 bridge_length와 같아지면 트럭빼기
                t_list.pop() # 시간을 더해줘야 할 것 같은데, 밑에 if, else 구문에서 시간을 넣어주면 된다.

            if (sum(t_list)+q_truck) <= weight :     # t_list의 합이 weight 이하이면 트럭을 계속 넣을 수 있다.
                t_list.insert(0,q_truck)
                q_truck = 0
                answer +=1
            else :
                t_list.insert(0,0)
                answer +=1

    # 마지막에 다리에 들어간 트럭이 나가는 시간 더해주기
    answer = answer + bridge_length
    print(answer)

    return answer

if __name__ == '__main__':

    bridge_length, weight, truck_weight = 2, 10, [7, 4, 5, 6]

    print(solution(bridge_length, weight, truck_weight))