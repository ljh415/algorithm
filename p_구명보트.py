import math

'''def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    idx = 1
    while len(people) != 0:
        if max(people) <= limit // 2:
            answer += math.ceil(len(people) / 2)
            return answer

        if len(people) == 1:
            return answer + 1

        for i in range(idx, len(people)):
            if people[0] + people[i] <= limit:
                people.pop(i)
                people.pop(0)
                answer += 1
                break
            elif i == len(people) - 1:
                people.pop(0)
                answer += 1
                break

    return answer'''

def solution(people, limit) :
    answer = 0
    people.sort()
    light, heavy = 0, len(people)-1

    while light <= heavy :
        if people[light] + people[heavy] <= limit :
            light += 1
            heavy -= 1
            answer += 1
        else :
            heavy -= 1
            answer += 1

    return answer


if __name__ == "__main__":
    # people, limit = [70, 50, 80, 50], 100
    people, limit = [70, 50, 80], 100

    print(solution(people, limit))