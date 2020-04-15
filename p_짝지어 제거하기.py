def solution(s):
    # s = list(s)
    stack = []

    for i in range(len(s)) :
        if len(stack) == 0 :
            stack.append(s[i])
            # continue
        elif stack[len(stack)-1] == s[i] :
            stack.pop(len(stack)-1)
        else :
            stack.append(s[i])

    if len(stack) == 0 :
        return 1
    else :
        return 0


if __name__ == '__main__':
    s = "baabaa"
    # s = "cdcd"

    print(solution(s))