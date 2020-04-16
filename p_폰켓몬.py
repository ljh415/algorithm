import itertools
from collections import Counter

def solution(nums) :
    answer = 0
    key_lst = []
    print(Counter(nums))
    key_lst = Counter(nums).keys()
    print(key_lst)

    n = len(nums)//2

    if len(key_lst) < len(nums)//2 :
        return len(key_lst)
    else :
        return len(nums)//2

if __name__ == '__main__':
    # nums = [3, 1, 2, 3]
    # nums = [3, 3, 3, 2, 2, 4]
    nums = [3, 3, 3, 2, 2, 2]
    print(solution(nums))