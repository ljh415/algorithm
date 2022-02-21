def solution(numbers):
    all = set(range(0, 10, 1))
    num_set = set(numbers)
    return sum(list(all-num_set))


if __name__=='__main__':

    input_args = [
        [1, 2, 3, 4, 6, 7, 8, 0],
        [5, 8, 4, 0, 6, 7, 9],
    ]
    for numbers in input_args:
        print(solution(numbers))