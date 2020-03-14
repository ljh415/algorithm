def solution(n):
    answer = ''

    while n > 0:
        n -= 1
        answer = '124'[n % 3] + answer
        n //= 3

    return answer

n = [1, 2, 3, 4]
for i in n :
    solution(i)