def solution(priorities, location):
    answer = 0
    check_flag = [0] * len(priorities)
    check_flag[location] = 1

    Max_in_lst = max(priorities)

    while True:

        if priorities[0] < Max_in_lst:
            p = priorities.pop(0)
            c = check_flag.pop(0)
            priorities.append(p)
            check_flag.append(c)

        elif check_flag[0] == 1:
            answer += 1
            return answer

        else:
            p = priorities.pop(0)
            c = check_flag.pop(0)
            answer += 1
            Max_in_lst = max(priorities)

    return answer