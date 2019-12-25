n = input()

if n == ' ' :
    print(0)
else :
    n = list(n.split(' '))

    while '' in n :
        n.remove('')

    print(len(n))