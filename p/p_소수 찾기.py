import itertools

# avg time : 391.9116
def make_sieve(n) :
    sieve = [True] * (n+1)
    m = int(n**0.5)
    for i in range(2, m+1):
        if sieve[i] == True:
            for j in range(i+i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]

def solution(numbers):
    answer = 0
    num_lst = []

    # 모든 경우의 수
    for i in range(len(numbers)):
        num_lst.extend([int(''.join(a)) for a in list(itertools.permutations(list(numbers), i + 1))])
    num_lst = list(set(num_lst))

    # 에라토스테네스의 체
    sieve = make_sieve(max(num_lst))
    # print(sieve)

    for num in num_lst :
        if num in sieve:
            answer +=1

    return answer


# avg time = 430.4458
def solution3(numbers):
    answer = 0
    num_lst = []

    # 모든 경우의 수
    for i in range(len(numbers)):
        num_lst.extend([int(''.join(a)) for a in list(itertools.permutations(list(numbers), i+1))])
    num_lst = list(set(num_lst))

    # 소수 만들기
    for num in num_lst :
        check_num = 0
        for i in range(1, num+1):
            if num % i == 0 :
                check_num+=1
            if check_num == 3 :
                break

        if check_num == 2:
            answer+=1

    return answer

# 이전 코드 => 테스트케이스 10번 통과 실패
# def makePermList(stringNumber):
#     p = []
#     perm_lst = []
#
#     for i in range(len(str(stringNumber))):
#         p += (list(itertools.permutations(str(stringNumber), i + 1)))
#
#     for a in p:
#         # print("")
#         l = ""
#         for i in range(len(a)):
#             # print("a = {}, a[{}] = {}\n".format(a, i, a[i]))
#             l += str(a[i])
#
#         if int(l) != 1 and int(l) != 0:
#             perm_lst.append(int(l))
#
#     perm_lst = sorted(list(set(perm_lst)))
#
#     return perm_lst
#
#
# def makePrimeNum(num_of_list):
#     print(num_of_list)
#
#     for i in range(2, num_of_list[len(num_of_list) - 1]):
#         for a in num_of_list:
#             if a % i == 0 and a != i:
#                 num_of_list.remove(a)
#
#     print(num_of_list)
#
#     return len(num_of_list)
#
#
# def solution(numbers):
#     answer = 0
#
#     pl = makePermList(numbers)
#     # print(pl)
#
#     return makePrimeNum(pl)


if __name__ == '__main__':
    numbers = "17"
    # numbers = "011"

    print(solution(numbers))

    # a = [1, 2, 3]
    # print(list(itertools.permutations(a, 1)))