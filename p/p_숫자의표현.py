def solution(n):
    answer = 0
    hap = 0
    idx = 1

    while idx != (n+1) :

        for i in range(idx, n+1) :
            if hap > n :
                hap = 0
                idx += 1
                break
            elif hap == n :
                answer += 1
                idx += 1
                hap = 0
                break
            else :
                hap += i

    return answer

if __name__ == "__main__" :
    n = 15

    print(solution(n))