def gcd(a, b) :

    if a < b :
        a, b = b, a

    while b!=0 :
        r = a % b
        a = b
        b = r

    return a

def lcm(a, b) :
    return a*b / gcd(a, b)


def solution(arr):
    answer = 0
    print(arr)

    for i in range(len(arr)) :
        if i < 1 :
            answer = arr[i]
            continue
        else :
            answer = lcm(answer, arr[i])

    return int(answer)

if __name__ == '__main__':
    arr = [2, 6, 8, 14]
    # arr = [1, 2, 3]

    print(solution(arr))