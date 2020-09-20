def solution(begin, target, words):
    answer = 0
    new_lst = []
    words = list(map(lambda x : list(x), words))
    for word in words :
        word = list(map(lambda x : ord(x), word))
        new_lst.append(sum(word))

    print(new_lst)
    # for i in range(len(words)):
    #     word = list(words[i])
    #     for j in range(len(word)):
    #

    return answer

if __name__ == '__main__':
    begin, target, words = 'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    # begin, target, words = 'hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']

    print(solution(begin, target, words))