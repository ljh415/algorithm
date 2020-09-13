import itertools

def solution4(number, k):

    lst = set()
    for a in list(itertools.combinations(number, len(number)-k)):
        #print(a)
        lst.add(''.join(a))

    answer = str(max(lst))

    return answer

def solution3(number, k):
    n = len(number) - k
    number = list(map(int, number))
    answer = {}
    answer_st = ''
    start = 0
    end = n

    while n > 0:

        print("start : {}, end : {}".format(start, end))
        print("n = {}".format(n))
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

def solution2(number, k):
    collected = []  # 숫자를 모아서 큰 수를 만들 때 쓰일 배열
    # 문자열에도 모을 수 있지만 문자열은 immutable(값이 변하지 않는)특성을 가지기에 코드 효율은 리스트(mutable)다 더 좋다
    # call by value , call by reference와 동일한 개념
    for i, num in enumerate(number):
        # k개 만큼의 숫자를 빼냈을 때, i의 인덱스를 기억하기 위해서 i를 사용
        while len(collected) > 0 and collected[-1] < num and k > 0:
            # 1. 맨 마지막 문자만 비교를 하면 될까? -> 그렇다. 지금까지 원칙을 지켜서 쌓아 왔다면 지금까지 쌓인 숫자들은 내림차순으로 되어있다.
            # 2. collected의 마지막 원소는 한 문자로 이루어진 문자열이다. num 또한 한 글자 짜리 문자열이다. 이걸 정수로 변환하지 않고,
            # 두개의 문자열에 대해서 대소관계를 이용해도 괜찮은가? -> 괜찮다. 알파벳 순서에 따르면 0은 1보다 작고, 3은 2보다 크고, 수의 크기 대소관계와 같다.
            # ※ 길이가 2 이상이라면, 사전에 나타난 숫자가 되겠지만, 지금은 한글자 짜리기 때문에 정수 변환이 필요없다.
            collected.pop()  # 리스트이 맨 끝에 있는 원소 하나를 없앤다.
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)
    collected = collected[:-k] if k > 0 else collected
    # k가 0 이면 빈 리스트가 되기 때문에 if를 이용해서 조건을 걸어준다.
    answer = ''.join(collected)
    return answer

def solution(number, k):
    length = len(number)
    if length > k:
        m = 0
        for cnt in range(k):
            for idx in range(m, length-1):
                if number[idx] < number[idx+1]:
                    number = number[:idx] + number[idx+1: ]
                    length -= 1
                    if idx > 0:
                        m = idx-1
                    break
            else:
                number = number[:length-k+cnt]
                break
        return "".join([str(i) for i in number])
    else:
        return "0"

if __name__ == '__main__':
    # number, k = "1924", 2
    # number, k =  "1231234", 3
    number, k = "4177252841", 4

    print(solution(number, k))

# 3번째 테스트케이스에서 에러
# 77겹치는 숫자 때문에 max값의 인덱스를 가져올때 이미 가져온 앞 부분의 7의 위치를
# 받아와서 계속 원하는 답이 안나온다.
# 어떻게 해결을 할까..? 그리디 알고리즘은 맞게 실행한 것 같은데
# 그렇다면 최대값까지 탐색하고나서 앞에부분을 지워버리면 될꺼같다.