## 정답
# def solution(records) :
#     answer = []
#     name_table = {}
#     caseList = []
#     actionList = {'Leave' : '님이 나갔습니다.', 'Enter' : '님이 들어왔습니다.'}
#     for record in records :
#         record = record.split(' ')
#         action = record[0]
#         if action != 'Leave':
#             #이름을 변경하거나 새로 생성
#             name_table[record[1]] = record[2]
#         if action != 'Change' :
#             caseList.append((action, record[1]))
#
#     for action, id in caseList :
#         answer.append(name_table[id] + actionList[action])
#
#     return answer
# 출처 : https://daimhada.tistory.com/165

## 내가 짠 코드

def solution(record):
    answer = []
    lst = []
    user_dict = {}

    for a in record:
        lst += [a.split(" ")]

    for b in lst :
        if b[0] == 'Enter':
            # if b[1] in user_dict :
            #     continue
            # else :
            user_dict[b[1]] = b[2]
            answer.append(''.join(b[1]+'님이 들어왔습니다.'))
            # print(answer)

        elif b[0] == 'Leave':
            answer.append(''.join(b[1]+'님이 나갔습니다.'))
            # print(answer)

        elif b[0] == 'Change':
            user_dict[b[1]] = b[2]

    for i in range(len(answer)):
        if list(user_dict.keys())[0] in answer[i]:
            answer[i] = answer[i].replace(list(user_dict.keys())[0], user_dict.get(list(user_dict.keys())[0]))
        elif list(user_dict.keys())[1] in answer[i]:
            answer[i] = answer[i].replace(list(user_dict.keys())[1], user_dict.get(list(user_dict.keys())[1]))


    print(answer)

    return answer

record = ['Enter uid1234 Muzi', 'Enter uid4567 Prodo',
          'Leave uid1234', 'Enter uid1234 Prodo',
          'Change uid4567 Ryan']

solution(record)