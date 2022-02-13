from collections import Counter

def solution(participant, completion):
    answer = ''

    participant = dict(Counter(participant))

    for comp in completion:
        participant[comp]-=1

    for key, value in participant.items():
        if value != 0 :
            return key

def solution2(participant, completion) :
    dic = {}
    dic = Counter(participant) - Counter(completion)
    # print(dic)

    return list(dic.keys())[0]

if __name__ == "__main__" :
    participant, completion = ['leo', 'kiki', 'eden'], ['eden', 'kiki']
    # participant, completion = ['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']
    # participant, completion = ['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']

    # print(solution(participant, completion))
    print(solution2(participant, completion))