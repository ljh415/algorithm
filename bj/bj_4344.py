C = int(input())
answer = []

for _ in range(C) :
    line = list(input().split(' '))
    N = int(line[0])
    score_lst = list(map(int, line[1:len(line)]))
    avg = sum(score_lst) / len(score_lst)
    cnt = 0
    for i in score_lst :
        if i > avg :
            cnt += 1
    ans = round(cnt / len(score_lst) * 100, 3)
    answer.append("%.3f" % ans + "%")

print('\n'.join(answer))