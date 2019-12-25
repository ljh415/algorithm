S = list(input())
hap = 0

for i in range(len(S)) :
    if ord(S[i]) >= 65 and ord(S[i]) < 68 :
        hap += 3
    elif ord(S[i]) < 71 :
        hap += 4
    elif ord(S[i]) < 74 :
        hap += 5
    elif ord(S[i]) < 77 :
        hap += 6
    elif ord(S[i]) < 80:
        hap += 7
    elif ord(S[i]) < 84 :
        hap += 8
    elif ord(S[i]) < 87 :
        hap += 9
    #elif ord(S[i]) < 92 :
    else :
        hap += 10

print(hap)