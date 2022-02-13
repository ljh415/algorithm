def solution(numbers):
    numbers = sorted(list(map(str, numbers)), reverse=True, key = lambda x : x*3)
    return str(int(''.join(numbers)))
    # return ''.join(numbers)

if __name__ == '__main__':
    # numbers = [6, 10, 2]
    # numbers = [3, 30, 34, 5, 9]
    numbers = [0, 0, 0, 0]

    print(solution(numbers))