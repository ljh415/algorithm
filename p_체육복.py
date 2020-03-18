def solution(n, lost, reserve):
    # n : 전체 학생수
    # lost : 도난 당한사람
    # reserve : 여벌을 가져온 사람

    answer = 0
    i = 0
    j = 0

    # 학생들의 배열을 1로 초기화
    students = [1] * n


    # 잃어버린 학생들의 배열에는 1을 빼준다
    while i < len(lost):
        students[lost[i] - 1] -= 1
        i += 1

    # 여유분이 있는 학생들의 배열에는 1을 더해준다
    while j < len(reserve):
        students[reserve[j] - 1] += 1
        j += 1


    #처음 학생이 체육복이 없다면
    if students[0] is 0:
        # 만약 두번째 학생이 체육복 여유가 있을 경우
        if students[1] is 2:
            students[1] -= 1
            students[0] += 1

    # 맨끝의 학생이 체육복이 없다면
    if students[n - 1] is 0:
        # 뒤에서 두번째 학생의 체육복이 여유가 있을 경우
        if students[n - 2] is 2:
            students[n - 2] -= 1
            students[n - 1] += 1

    # 2번째 ~ 뒤에서 2번째
    for i in range(1, n - 1):
        # 탐색하는 학생의 체육복이 없을 경우
        if students[i] is 0:
            # 앞에 학생이 체육복이 여분이 있다면 한벌을 가져오고
            if students[i - 1] is 2:
                students[i - 1] -= 1
                students[i] += 1
            # 앞에 학생이 여유가 없다면 뒤에 학생에게 옷을 빌려온다
            elif students[i + 1] is 2:
                students[i + 1] -= 1
                students[i] += 1

    # 전체를 확인하면서 체육복수가 0이 아닌 수를 확인하면서 answer를 하나씩 늘려감
    for i in range(len(students)):
        if students[i] is not 0:
            answer += 1

    print(students)

    return answer

if __name__ == "__main__" :
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]

    # n = 5
    # lost = [2, 4]
    # reserve = [3]

    # n = 3
    # lost = [3]
    # reserve = [1]

    print(solution(n, lost, reserve))