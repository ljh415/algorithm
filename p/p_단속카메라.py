def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x : x[1])
    print(routes)
    prev_end = -30000

    for start, end in routes :
        # 겹쳐지는 부분이 없을 경우 answer를 하나 증가
        # 카메라 += 1
        if prev_end < start :
            answer += 1
            prev_end = end

    return answer

if __name__ == '__main__':
    routes = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]

    print(solution(routes))



'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.2MB)
테스트 2 〉	통과 (0.02ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10.2MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.03ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (0.64ms, 10.5MB)
테스트 2 〉	통과 (0.37ms, 10.3MB)
테스트 3 〉	통과 (1.00ms, 10.6MB)
테스트 4 〉	통과 (0.05ms, 10.1MB)
테스트 5 〉	통과 (1.07ms, 10.6MB)
'''