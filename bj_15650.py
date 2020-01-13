import itertools

N, M = map(int, input().split(' '))

lst = []

for i in range(N) :
    lst.append(i+1)

if M == 1 :
    for a in lst :
        print(a)
else :
    lst_comb = list(itertools.combinations(lst, M))
    for y in lst_comb :
        for b in y :
            print(b, end=' ')
        print()
