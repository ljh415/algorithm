# import itertools
#
# def solution(number, k):
#
#     lst = set()
#     for a in list(itertools.combinations(number, len(number)-k)):
#         #print(a)
#         lst.add(''.join(a))
#
#     answer = str(max(lst))
#
#     return answer

def solution(number, k):
    n = len(number) - k
    number = list(map(int, number))
    answer = {}
    answer_st = ''
    start = 0
    end = n

    while n > 0:

        # print("start : {}, end : {}".format(start, end))
        # print("n = {}".format(n))
        if start != end:
            answer[n] = max(number[start:end])
            del number[0:number[start:end].index(max(number[start:end]))+1]
            # print(number)
        else:
            answer[n] = number[start]

        n -= 1
        end = len(number) - n + 1

    answer_idx = list(reversed(sorted(answer)))

    for x in answer_idx:
        answer_st += str(answer[x])

    return answer_st

# number = "1924"
# number =  "1231234"
number = "4177252841"

# k = 2
# k = 3
k = 4

print(solution(number, k))

# 3번째 테스트케이스에서 에러
# 77겹치는 숫자 때문에 max값의 인덱스를 가져올때 이미 가져온 앞 부분의 7의 위치를
# 받아와서 계속 원하는 답이 안나온다.
# 어떻게 해결을 할까..? 그리디 알고리즘은 맞게 실행한 것 같은데
# 그렇다면 최대값까지 탐색하고나서 앞에부분을 지워버리면 될꺼같다.