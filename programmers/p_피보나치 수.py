import sys
sys.setrecursionlimit(10**6)

lst = [0] * 100001

def solution(n):
    answer = 0
    lst[1] = 1
    lst[2] = 1
    # print(lst)
    if n <= 2:
        return lst[n]
    else:
        if lst[n] != 0:
            return lst[n] % 1234567
        else:
            lst[n] = solution(n-1) + solution(n-2)
            return lst[n] % 1234567

    # return answer

if __name__ == "__main__" :
    # n = 3
    # n = 5
    n = 100000

    print(solution(n))