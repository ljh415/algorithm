'''def solution(citations) :
    citations.sort()
    tmp = []


    for a in citations :
        up = 0
        for i in range(len(citations)) :
            if a <= citations[i] :
                up += 1
        if up >= a :
            tmp.append(a)

    return max(tmp)'''


def solution(citations) :
    for i, x in enumerate(sorted(citations)) :
        if x >= len(citations) - i :
            return len(citations) - i
    return 0

if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    # citations = [1,3,4,6,7,8]
    print(solution(citations))