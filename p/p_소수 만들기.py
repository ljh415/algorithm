import itertools

def solution(nums):
    answer = 0
    sum_lst = []
    # flag = False

    # print(list(itertools.combinations(nums, 3)))

    for a in list(itertools.combinations(nums, 3)) :
        # print(sum(a))
        sum_lst.append(sum(a))
    # print("길이 : ", len(sum_lst))

    for b in sum_lst :
        flag = True
        for i in range(2, b-1) :
            if b % i == 0 :
                flag = False
                break
        if flag :
             answer+=1

    return answer

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    # nums = [1, 2, 7, 6, 4]

    print(solution(nums))