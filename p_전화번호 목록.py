def solution(phone_book) :
    answer = True
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)) :
        for j in range(i+1, len(phone_book)-1) :
            if str(j) in str(i) :
                return False
    return True

if __name__ == "__main__" :
    # phone_book =    ['119', '97674223', '1195524421']
    # phone_book = ['123', '456', '789']
    phone_book = ['12', '123', '1235', '567', '88']

    print(solution(phone_book))