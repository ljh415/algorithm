N = int(input())
lst = []

for _ in range(N) :
    lst.append(list(map(int, input().split(' '))))

lst.sort()

for a in range(len(lst)) :
    for b in range(2) :
        print(lst[a][b], end=' ')
    print()