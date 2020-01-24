# 원래 짰던 코드
'''
def fibo(n) :

    if n < 2 :
        return n
    else :
        return fibo(n-1)+fibo(n-2)

n = int(input())
print(fibo(n))
'''


n = int(input())

pi = [0] * (n+1)
pi[1] = 1

if n < 2 :
    print(pi[n])
else :
    for i in range(2, n+1) :
        pi[i] = pi[i-1] + pi[i-2]
    print(pi[n])