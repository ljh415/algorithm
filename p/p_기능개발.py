import math


def solution(progresses, speeds):
    answer = []
    count = 0
    key = 0

    progresses = [100 - a for a in progresses]
    for i in range(len(progresses)):
        progresses[i] = math.ceil(progresses[i] / speeds[i])

    while len(progresses) > 0:

        a = progresses[0]
        if key < progresses[0]:
            key = progresses[0]
            if count != 0 :
                answer.append(count)
                count = 0


        elif a <= key:
            progresses.pop(0)
            count += 1
        else:
            progresses.pop(0)
            count += 1
            answer.append(count)
            count = 0
    answer.append(count)


    print(answer)

    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]


solution(progresses, speeds)