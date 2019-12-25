a, b = input().split(' ')

a = int(''.join(reversed(list(a))))
b = int(''.join(reversed(list(b))))

if a > b :
    print(a)
else :
    print(b)