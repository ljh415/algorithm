n = int(input())

pi = [0] * (n+1)
pi[1] = 1

if n < 2 :
    print(pi[n])
else :
    for i in range(2, n+1) :
        pi[i] = pi[i-1] + pi[i-2]
    print(pi[n])

# 2747번과 같다