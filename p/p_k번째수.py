def solution(array, commands):
    answer = []

    for a in commands :
        answer.append(sorted(array[(a[0]-1) : a[1]], reverse = False)[a[2]-1])

    return answer