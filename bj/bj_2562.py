list = list(map(int, list(input() for _ in range(9))))

print(max(list))
print(list.index(max(list))+1)