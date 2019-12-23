A, B, C = (int(input()) for _ in range(3))

total_num = A * B * C
total_num = list(map(int, (list(str(total_num)))))

for i in range(10) :
    print(total_num.count(i))