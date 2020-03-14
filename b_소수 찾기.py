import itertools


def makePermList(stringNumber):
    p = []
    perm_lst = []

    for i in range(len(str(stringNumber))):
        p += (list(itertools.permutations(str(stringNumber), i + 1)))

    for a in p:
        # print("")
        l = ""
        for i in range(len(a)):
            # print("a = {}, a[{}] = {}\n".format(a, i, a[i]))
            l += str(a[i])

        if int(l) != 1 and int(l) != 0:
            perm_lst.append(int(l))

    perm_lst = sorted(list(set(perm_lst)))

    return perm_lst


def makePrimeNum(num_of_list):
    print(num_of_list)

    for i in range(2, num_of_list[len(num_of_list) - 1]):
        for a in num_of_list:
            if a % i == 0 and a != i:
                num_of_list.remove(a)

    print(num_of_list)

    return len(num_of_list)


def solution(numbers):
    answer = 0

    pl = makePermList(numbers)
    # print(pl)

    return makePrimeNum(pl)


number = "17"
# number = "011"

solution(number)
