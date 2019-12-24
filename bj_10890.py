S = list(input())
S_t = {}
alp = {}

for index, value in enumerate(S) :
    if value in S_t.keys() :
        continue
    S_t[value] = index

for i in range(97, 123, 1) :
    alp[chr(i)] = -1

for j in S_t.keys() :
    if j in alp :
        alp[j] = S_t.get(j)

print(" ".join(list(map(str, alp.values()))))