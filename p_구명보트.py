'''
그리디, 구명보트를 최다한 적게 사용하여 모든 사람들을 구출
'''

import math

'''def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)
    print(people)
    hap = []
    idx = 0

    while len(people) != 0:
        if len(hap) == 0:
            hap.append(people.pop(0))

        for i in range(idx, len(people)) :
            if sum(hap) + people[i] > limit :
                if i == len(people)-1 :
                    hap.clear()
                    answer += 1
                    break
            elif len(hap) < 2 :
                people.pop(i)
                hap.clear()
                answer += 1
                break

    if len(hap) != 0 :
        answer += 1

    return answer'''

def solution(people, limit) :
    answer = 0
    people = sorted(people, reverse=True)
    idx = 1
    while len(people) != 0 :
        if len(people) == 1:
            return answer+1

        if max(people) <= limit//2 :
            answer += int(math.ceil(len(people) / 2))
            return answer

        for i in range(idx, len(people)):
            if people[0] + people[i] <= limit:
                people.pop(i)
                people.pop(0)
                answer += 1
                break
            elif i == len(people)-1:
                people.pop(0)
                answer += 1
                break

    return answer

if __name__ == "__main__" :
    people, limit = [70, 50, 80, 50], 100
    # people, limit = [70, 80, 50], 100
    # people, limit = [20, 24, 2, 3, 5, 7, 10, 29], 50


    print(solution(people, limit))