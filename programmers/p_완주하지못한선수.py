'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys()))
    return list(answer.keys())[0]'''

def solution(phone_book) :
    answer = True
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)) :
        for j in range(i+1, len(phone_book)-1) :
            if phone_book[i] in phone_book[j] :
                return False
    return True

if __name__ == "__main__" :
    # phone_book =    ['119', '97674223', '1195524421']
    # phone_book = ['123', '456', '789']
    phone_book = ['12', '123', '1235', '567', '88']

    print(solution(phone_book))