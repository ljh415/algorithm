def solution(absolutes, signs):
    answer = 0
    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else :
            answer -= num
    return answer



if __name__ == '__main__':
    input_data = [
        ([4, 7, 12], [True, False, True]),
        ([1, 2, 3], [False, False, True]),
    ]
    
    for absolutes, signs in input_data:
        print(solution(absolutes, signs))