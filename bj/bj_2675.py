T = int(input())

for a in range(T) :
    R, S = input().split(' ')
    R = int(R)
    S = list(S)
    str = []

    for i in range(len(S)) :
        for _ in range(R) :
            str.append(S[i])

    print("".join(str))