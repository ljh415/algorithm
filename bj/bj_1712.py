A, B, C = map(int, input().split(' '))

x = 0

if B<C :
    x = A // (C-B)
    print(x+1)
else :
    print(-1)