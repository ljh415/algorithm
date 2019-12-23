list = []

for _ in range(10) :
    list.append(int(input()) % 42)

list = set(list)

print(len(list))