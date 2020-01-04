N = int(input())
ans = N

for x in range(N) :
    str_x = str(x)
    hap = x
    for i in range(len(str_x)) :
        hap += int(str_x[i])
    #print("hap : {}, N : {}".format(hap, N))
    if hap == N and ans > x:
        ans = x
        print(ans)

if ans == N :
    print(0)

