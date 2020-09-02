# test case avg time : 2.6792
def solution2(answers):
    answer = []
    score = [0, 0, 0]
    student = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

    for idx, an in enumerate(answers) :
        for i in range(0, len(student)) :
            if an == student[i][idx%len(student[i])] :
                score[i] += 1

    for idx, s in enumerate(score) :
        if s == max(score) :
            answer.append(idx+1)

    return answer

# test case avg time : 1.7614
def solution(answers):
    answer = []
    result = {1 : 0, 2 : 0, 3 : 0}
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)) :
        if answers[i] == pattern_1[i%len(pattern_1)] :
            result[1] += 1

        if answers[i] == pattern_2[i%len(pattern_2)] :
            result[2] += 1

        if answers[i] == pattern_3[i%len(pattern_3)] :
            result[3] += 1

    for student, correct in result.items():
        if max(result.values()) == correct :
            answer.append(student)
    # print(result)
    return answer

if __name__ == '__main__':
    # answers = [1,2,3,4,5]
    answers = [1,3,2,4,2]

    print(solution1(answers))