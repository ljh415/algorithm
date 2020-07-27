N = int(input())

score = list(map(int, list(input().split(' '))))

Max = max(score)
for i in range(len(score)) :
    score[i] = score[i]/Max*100

print('%.2f' % (sum(score) / len(score)))