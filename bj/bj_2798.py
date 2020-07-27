N, M = map(int, input().split(' '))
card = list(map(int, list(input().split())))
temp=0

for x in range(len(card)-2) :
    for y in range(x+1, len(card)-1) :
        for z in range(y+1, len(card)) :
            hap = card[x] + card[y] + card[z]
            if hap <= M and temp < hap :
                temp = hap

print(temp)