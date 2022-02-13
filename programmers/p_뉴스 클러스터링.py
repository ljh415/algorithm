# def bigram(str) :
#     str_lst = []
#
#     two_gram = zip(str, str[1:])
#     for i in two_gram :
#         str_lst.append(i[0]+i[1])
#
#     str_lst = check_str(str_lst)
#
#     # print("bigram : ", str, " : ", str_lst)
#
#     return str_lst
#
# def check_str(str_lst) :
#
#     flag = False
#
#     for i in range(len(str_lst)-1, -1, -1) :
#         for j in str_lst[i] :
#             if not ord(j) >= 97 and ord(j) <= 122 :
#                 flag = True
#                 break
#         if flag :
#             str_lst.pop(i)
#             flag = False
#
#     return str_lst
#
# def intersection(lst1, lst2) :
#
#     ret = []
#
#     if len(lst1) > len(lst2) :
#         lst2, lst1 = lst1, lst2
#
#     for a in lst1 :
#         if a in lst2 :
#             ret.append(a)
#
#     return ret
#
# def union(lst1, lst2) :
#     ret = lst1 + lst2
#
#     for a in intersection(lst1, lst2) :
#         for i in range(len(ret)) :
#             if a == ret[i] :
#                 ret.pop(i)
#                 break
#
#     return ret
#
# def solution(str1, str2):
#     answer = 0
#     flag = False
#
#     str1 = str1.lower()
#     str2 = str2.lower()
#
#     str1_lst = bigram(str1)
#     str2_lst = bigram(str2)
#
#     inte = intersection(str1_lst, str2_lst)
#     unio = union(str1_lst, str2_lst)
#     # print(inte, unio)
#
#     if len(unio) == 0 or len(inte) == 0:
#         return 65536
#     else :
#         answer = int(len(inte) / len(unio) * 65536)
#
#     return answer

def str_split(string) :
    res = []
    for i in range(len(string)-1) :
        if string[i].isalpha() and string[i+1].isalpha() :
            res.append(string[i:i+2])
    return sorted(res)
# split를 활용해서 잘 나눴다.. 기존에 zip을 쓰는 것보다도 이게 좀 더 직관족으로 알기는 쉬운 것 같다
# str에는 isalpha() 를 활용해서 알파벳인지 아닌지 확인

def jaccard_index(lst, res = [], i=0, j=0) :
    if len(lst[0]) == 0 or len(lst[1]) == 0 :
        return 65536
    else :
        for i in lst[0] :
            if i in lst[1] :
                lst[1].remove(i)   # 차집합을 만들어서 이후에 더해줌으로써 합집합으로 표현
                res.append(i)      # 둘다 있을 경우 더해지는 거니까 교집합을 나타냄
        return int(len(res)/len(lst[0]+lst[1])*65536)
    # 분모의 lst[0] + lst[1]은 두 str의 합집합


def solution(str1, str2) :

    lst = []

    lst.append(str1.lower())
    lst.append(str2.lower())

    lst = list(map(str_split, lst))
    res = jaccard_index(lst)

    return res

if __name__ == '__main__':
    # str1, str2 = 'FRANCE', 'french'
    # str1, str2 = 'handshake', 'shake hands'
    str1, str2 = 'aa1+aa2', 'AAAA12'
    # str1, str2 = 'E=M*C^2', 'e=m*c^2'

    print(solution(str1, str2))
