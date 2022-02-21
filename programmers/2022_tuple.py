# https://programmers.co.kr/learn/courses/30/lessons/64065
# 순서있는 열거, 또는 어떤 순소를 따르는 요소들의 모음 -> 튜플

def solution(s):
    answer = []
    s = s.replace("{{", "").replace("}}", "").split("},{")
    s = list(map(lambda x: x.split(","), s))
    s = [list(map(int, x)) for x in s]
    
    s = sorted(s, key = lambda x : len(x))
    
    for s_in in s:
        s_in = sorted(s_in)
        for ss in s_in:
            if ss not in answer:
                answer.append(ss)

    return answer


if __name__ == '__main__':
    input_args = [
        # "{{2},{2,1},{2,1,3},{2,1,3,4}}",
        "{{1,2,3},{2,1},{1,2,4,3},{2}}",
        # "{{20,111},{111}}",
        # "{{123}}",
        # "{{4,2,3},{3},{2,3,4,1},{2,3}}"
    ]

    for s in input_args:
        print(solution(s))
        print()