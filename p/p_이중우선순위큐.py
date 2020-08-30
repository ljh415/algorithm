import heapq
import numpy as np

def tempfunc(lst) :
    np_arr = np.array(lst)
    np_arr *= -1
    lst = np_arr.tolist()
    return lst


def solution(operations):
    answer = []

    for operation in operations :
        op, num = operation.split(' ')
        if op == "I" :
            answer.append(int(num))
        else :
            if num == '1' :
                answer = tempfunc(answer)
                heapq.heapify(answer)
                try :
                    heapq.heappop(answer)
                except :
                    pass
                answer = tempfunc(answer)
            else :
                heapq.heapify(answer)
                try:
                    heapq.heappop(answer)
                except:
                    pass

    if not answer :
        return [0, 0]
    else :
        return [max(answer), min(answer)]

def solution2(operations) :  # 이게 더 빠름
    answer = []
    func = lambda x : (-1)*x #[a * (-1) for a in x]

    for operation in operations :
        op, num = operation.split(' ')
        if op == "I" :
            answer.append(int(num))
        else :
            if num == '1' :
                answer = list(map(func, answer))
                heapq.heapify(answer)
                try :
                    heapq.heappop(answer)
                except:
                    pass
                answer = list(map(func, answer))
            else :
                heapq.heapify(answer)
                try :
                    heapq.heappop(answer)
                except :
                    pass

    if not answer :
        return [0, 0]
    else :
        return [max(answer), min(answer)]


if __name__ == '__main__':
    # operations = ["I 16","D 1"]
    # operations = ["I 7","I 5","I -5","D -1"]
    # operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
    # [0, 0]
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    # [333, -45]

    print(solution2(operations))