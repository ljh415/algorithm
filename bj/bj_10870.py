n = int(input())
fib = []

def fibo(a) :
    if a <= 1 :
        return a
    elif a == 2 :
        return 1
    else :
        return fibo(a-1)+fibo(a-2)

print(fibo(n))