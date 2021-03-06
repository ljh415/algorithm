def solution2(name):
    answer = 0
    name = list(name)
    answers = []

    # print("A={} ~ Z={}".format(ord("A"), ord("Z")))

    for i in range(len(name)):
        code = 65  # A를 나타내는 unicode로 초기화
        if name[i] != "A" :
            while name[i] != chr(code):   # A에서 시작, name의 i번째의 알파벳과 같아지면 while문 탈출
                if ord(name[i]) <= 78:    # A에서 시작하지만 만약 중간에 위치하는 N 전의 알파벳이라면 아스키코드를 하나씩 더해간다
                    code += 1
                    answer += 1
                else:                     # N 후에 있는 알파벳이라면 코드를 줄여나가고 만약 65보다 작아진다면("A") code변수를 Z의 아스키코드로 바꿔준다.
                    code -= 1
                    if code < 65:
                        code = 90
                    answer += 1
            if i != (len(name)-1):     # 알파벳하고 code를 맞추고 나서 마지막 자리가 아니라면?
                answer += 1            # 다음 오른쪽 자리로 가야하기때문에..
        else :
            answer += 1
        # code의 아스키코드는 알파벳과 동일 하다면 지금 이 위치에 있을 것이고
        # 알파벳을 찾은후에는 자리 수를 옮겨야 하니깐 여기서 answer+1을 해주는데..

    answers.append(answer)

    ## 거꾸로..탐색
    answer = 0
    for i in range(0, -len(name), -1):
        code = 65  # A를 나타내는 unicode로 초기화
        if name[i] != "A" :
            while name[i] != chr(code):
                if ord(name[i]) <= 78:
                    code += 1
                    answer += 1
                else:
                    code -= 1
                    if code < 65:
                        code = 90
                    answer += 1
            if i != -(len(name)-1) : # and name[-(len(name)-1)] == "A" :
                answer += 1
                # break
        elif i == -(len(name)-1) :
            answer -= 1

    answers.append(answer)

    return min(answers)

def solution(name):
    answer = 0
    name = list(name)
    index = 0
    while(True) :
        right = 1
        left = 1
        if name[index] != 'A' :
            updown = min(ord(name[index]) - ord('A'), ord('Z')-ord(name[index])+1)
            answer += updown
        name[index] = 'A'

        # 탈출조건
        if name == ["A"] * len(name) : break

        # 이 부분이 중요했다..
        # 현재 위치에서 오른쪽, 왼쪽 방향을 선택
        # 오른쪽으로 탐색
        # A가 아닌 문자를 찾는다
        for i in range(1, len(name)):
            if name[index+i] == 'A' :
                right += 1
            else :
                break

        # 왼쪽으로 탐색다
        # A가 아닌 문자를 찾는다
        for i in range(1, len(name)):
            if name[index-i] == 'A' :
                left += 1
            else :
                break

        if right>left :
            answer += left
            index -= left
        else :
            answer += right
            index += right

    return answer

if __name__ == "__main__" :
    name = "JEROEN"
    # name = "JAN"
    # name = "AAB"

    print(solution(name))