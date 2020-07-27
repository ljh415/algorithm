N = int(input())

lst = []
for _ in range(N) :
    lst.append(int(input()))

for i in sorted(lst) :
    print(i)