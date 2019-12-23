N = int(input())

for i in range(N) :
    line = list(input())
    SUM = 0
    cnt = 0
    for j in range(len(line)) :
        if line[j] == 'O' :
            cnt += 1
            SUM += cnt
        else :
            cnt = 0
    print(SUM)