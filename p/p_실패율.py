def solution(N, stages):
    answer = {}
    people_in_stage = [0] * (N+1)
    people_clear_stage = [0] * (N+1)

    for a in stages :
        people_in_stage[a-1] +=1
        for b in range(a) :
            people_clear_stage[b] += 1

    for i in range(N) :
        people_clear_stage[i] = len(stages) - sum(people_in_stage[:i])

    err_rate = []
    for i in range(len(people_in_stage)-1):

        if people_clear_stage[i] == len(people_in_stage) and people_in_stage[i] == 0:
            # 모든사람이 클리어 했을 경우
            err_rate.append(0)
        elif people_in_stage[i] == 0:
            # 도달한 사람이 없을 경우
            err_rate.append(0)
        else:
            try :
                err_rate.append(people_in_stage[i]/people_clear_stage[i])
            except ZeroDivisionError :
                # 0으로 나눠질때, 도달한사람은 있지만 클리어를 못한다면 1
                err_rate.append(1)

    for idx, err in enumerate(err_rate):
        answer[idx+1] = err

    answer = dict(sorted(answer.items(), key=lambda item:item[1], reverse=True))

    return list(answer.keys())