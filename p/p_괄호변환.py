import copy
answer = ''

# 입력받은 문자열을 u : 더이상 분리 안되는 균형잡힌 문자열
# v : 나머지 문자열 (빈문자열 가능), 두개로 return
def func_A (w) :
    counter = 0

    for i in range(len(w)) :

        if w[i] == '(' :
            counter += 1
        else :
            counter -= 1

        if counter == 0 :
            u = w[0:i + 1]
            v = w[i+1:len(w)]
            return u, v

def check_right_str(u) :
    lst = []

    for i in range(len(u)) :
        if len(lst) == 0 :
            lst.append(u[i])
        elif u[i] == '(' :
            lst.append(u[i])
        elif lst[len(lst)-1] == '(' :
            lst.pop(len(lst)-1)
        else :
            lst.append(u[i])

    if len(lst) == 0 :
        return True
    else :
        return False

def func_B (u, v) :
    global answer

    flag = check_right_str(u)

    # 올바른 괄호 문자열
    if flag :
        answer += u
        print("찐")
        return solution(v)
    # 올바르지 않은 괄호 문자
    else :
        print('니은')
        tmp_str = '('
        tmp_u, tmp_v = func_A(v)
        tmp_str += tmp_u
        tmp_str += ')'
        for i in range(len(u)) :
            if u[i] == '(' :
                u[i] = ')'
            else :
                u[i] = '('
        answer = answer + tmp_str + u
        return answer


def solution(p) :
    global answer

    u, v = func_A(p)
    print(u, v)
    func_B(u, v)

    return answer

if __name__ == '__main__':
    p = "(()())()"
    # p = ")("
    # p = "()))((()"

    print(solution(p))

# 미완료