# def solution(s):
#     answer = ''
#     s_dic = {}
#     key, counter = "", 0
#     # length = len(s)
#
#     for i in range(len(s)) :
#         if i == 0 :
#             key = s[i]
#         if key == s[i] :
#             counter += 1
#         else :
#             s_dic[key, i] = counter
#             counter = 0
#             key = s[i]
#             counter += 1
#     s_dic[key, i] = counter
#
#     value_lst = list(s_dic.values())
#     key_lst = []
#     key = list(s_dic.keys())
#     for i in range(len(key)):
#         key_lst.append(key[i][0])
#         if value_lst[i] == 1:
#             answer = answer + key[i][0]
#         else:
#             answer = answer + key[i][0] + str(value_lst[i])
#
#     # print(s_dic)
#     # print(key_lst)
#     # print(value_lst)
#
#     return len(answer)

# def solution(s) :
#     answer = 0
#     length = len(s)
#     length //= 2
#     pattern_lst = []
#     temp_str = ""
#     temp_s = s
#
#     # 패턴의 길이 먼저 : 1 ~ length//2
#     for x in range(length, 0, -1):  # 길이
#         for y in range(0, len(s)-x):  # 시작점
#             temp_str = s[y:y+x]
#             if temp_str not in pattern_lst:
#                 pattern_lst.append(temp_str)
#                 temp_str = ""
#
#     for a in pattern_lst:
#         print(a)
#         pattern_counter = 1
#         # if a in temp_s :
#         #     patter_counter += 1
#         #     if patter_counter > 1 :
#         #         temp_s = temp_s.replace(a, str(patter_counter)+a)
#         for i in range(len(temp_s)-len(a)):
#             temp_s = s
#             # pattern_counter = 0
#             if s[i : len(a)] == a:
#                 pattern_counter += 1
#                 if pattern_counter > 1:
#                     temp_s = temp_s.replace(temp_s[i:len(a)], str(pattern_counter)+a)
#                     pattern_counter = 1
#         print(temp_s)
#         print(len(temp_s))
#
#     print(pattern_lst)
#
#     return answer

# def solution(s) :
#     answers = []
#
#
#     return answers


def solution(s) :
    answers = []  # 길이만 저장시킬 answers배열

    if len(s) == 1 :   # 문자열의 길이가 1이면 1을 그대로 반환
        return 1
    for i in range(1, len(s)) :     # 문자열의 길이가 1보다 길면, i는 1부터 s의 길이만큼 반복
        answer = ''                 # aabbaccc => 2a2ba3c형식으로 저장시킬 빈문자열
        count = 1                   # count의 초기값은 1
        for j in range(i, len(s), i) :
            # i는 탐색할 문자열의 길이를 뜻하는 것 같다. 만약 i=2면 길이가 2인 문자열들을 비교하는데
            # j는 i부터 시작해서 늘 시작은 j-i = 0으로 맨앞부터 탐색을 시작
            # 만약에 i = 2이라고 하고 위의 반복문이 실행될때
            # s[0:2](비교할 pattern) == s[2:4]
            # s[2:4](비교할 pattern) == s[4:6]
            # 일치하는 문자열을 발견한다면 count를 하나씩 늘려주고
            if s[j-i:j] == s[j:j+i] :
                count += 1
            else:
                # 지금 문자열하고 바로 다음인덱스부터를 비교해서 다르다면?
                # count가 1인 경우에는 answer에 그대로 입력
                if count == 1:
                    answer+=s[j-i:j]
                # count가 1이 아닌수라면? = 겹쳐지는 수라면
                # answer 문자열에 숫자 + pattern을 입력
                # 그리고 count는 다시 1로 초기화
                else:
                    answer += str(count) + s[j-i:j]
                    count = 1

        # 위에 반복문에서 해당 원하는 길이의 패턴을 탐색을 다하고나서...?
        # 디버깅을 찍어보면 마지막 부분이 안들어간다
        # 위에 if count == 1 부분과 같이 count를 확인해서 1이면 마지막 탐색하는 단어를 그냥 넣고
        # 아니면 숫자+마지막으로 탐색하는 문자를 같이 넣어준다
        if len(s[j:j+i]) == i:
            if count==1:
                answer += s[j-i:j]
            else:
                answer += str(count)+s[j-i:j]
                count = 1
        else:
            answer += s[j:j+i]
        answers.append(len(answer))

    return min(answers)   # 이후에 min을 사용해서 길이중 가장 짧은 값을 반환

if __name__ == "__main__" :
    s = "aabbaccc"
    # s = "ababcdcdababcdcd"
    # s = "abcabcdede"
    # s = "abcabcabcabcdededededede"
    # s = "xababcdcdababcdcd"

    print(solution(s))