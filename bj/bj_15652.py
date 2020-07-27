'''import itertools

N, M = map(int, input().split(' '))
temp = 0
lst = []
flag = True

for i in range(N) :
    lst.append(i+1)

if M == 1 :
    for a in lst :
        print(a)
else :
    lst_comb = list(itertools.product(lst, repeat = M))

    for y in lst_comb :
        for i in range(len(y)) :
            if i == 0 :
                temp = y[i]
            elif temp <= y[i] :
                temp = y[i]
            else :
                flag = False

        if flag :
            for b in y :
                print(b, end=' ')
            print('')
        else :
            flag = True'''

import itertools

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]

for num in itertools.combinations_with_replacement(num_list, M) :
    for i in num :
        print(i, end = ' ')
    print('')