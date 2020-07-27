import math

def solution(brown, red):
    answer = []
    length_lst = []

    s = brown + red
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
    brown, red = 10, 2
    # brown, red = 8, 1
    # brown, red = 8, 6

    print(solution(brown, red))