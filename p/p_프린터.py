def solution(priorities, location):
    answer = 0
    # 원하는 문서에 대한 위치를 저장
    check_flag = [0] * len(priorities)
    check_flag[location] = 1

    max_in_lst = max(priorities)

    while True:
        # 우선순위가 가장 높은 문서가 0번 인덱스에 올떄까지 반복
        if priorities[0] < max_in_lst:
            p = priorities.pop(0)
            c = check_flag.pop(0)
            priorities.append(p)
            check_flag.append(c)

        # 원하는 문서를 출력해야 할때 answer를
        # 하나 증가시키면서 return 으로 종료
        elif check_flag[0] == 1:
            answer += 1
            return answer

        # 우선순위문서를 출력하면서 answer증가
        # 그다음 우선순위값을 max_in_lst에 증가
        else:
            p = priorities.pop(0)
            c = check_flag.pop(0)
            answer += 1
            max_in_lst = max(priorities)

if __name__ == '__main__':

    priorities, location = [2, 1, 3, 2], 2
    # priorities, location = [1, 1, 9, 1, 1, 1], 0

    print(solution(priorities, location))