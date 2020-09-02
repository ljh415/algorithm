# avg time = 0.2823
def solution(brown, yellow):

    brown_case = []
    # brown의 경우의 수 탐색
    brown = (brown // 2) + 2
    for i in range(3, brown//2+1) :
        brown_case.append((brown-i, i))

    # yellow 경우의 수 확인
    for garo, sero in brown_case:
        if (garo-2)*(sero-2) == yellow :
            return [garo, sero]


import math

# avg time = 29.4376
def solution2(brown, yellow):
    answer = []
    length_lst = []

    s = brown + yellow
    for i in range(1, s + 1):
        if s % i == 0 and i not in length_lst:
            length_lst.append(i)
    print(length_lst)

    for i in range(math.ceil(len(length_lst)/2)) :
        a = length_lst[i]
        b = s // a
        print("a = {}, b = {}".format(a, b))
        if (a+b-2) * 2 <= brown :
            if a > b : answer.append([a, b])
            else : answer.append([b, a])
        else :
            continue

    '''
    mid = len(answer) // 2
    a = s // answer[mid]
    b = answer[mid]
    '''

    return answer[0]

if __name__ == "__main__" :
    brown, yellow = 10, 2
    # brown, yellow = 8, 1
    # brown, yellow = 8, 6
    # brown, yellow = 24, 24

    print(solution(brown, yellow))