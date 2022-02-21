# https://programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []

    while progresses:
        while progresses[0] < 100:
            for idx, s in enumerate(speeds):
                if progresses[idx] >= 100 :
                    continue
                progresses[idx]+=s
        cnt = 0
        for p in progresses:
            if p >= 100:
                cnt += 1
            else :
                break
        progresses = progresses[cnt:]
        speeds = speeds[cnt:]
        answer.append(cnt)

    return answer

if __name__ == '__main__':
    input_args = [
        ([93, 30, 55], [1, 30, 5]),
        ([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
    ]

    for progresses, speeds in input_args:
        print(solution(progresses, speeds))