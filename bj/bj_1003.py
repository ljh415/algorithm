'''zero = 0
one = 1

def fibonacci(n, lst) :
    global memo
    if n == 0 :
        lst.append(0)
        return 0
    elif n == 1 :
        lst.append(1)
        return 1
    else :
        if n in memo :
            return memo[n]
        else :

            return fibonacci(n-1, lst) + fibonacci(n-2, lst)


T = int(input())

for _ in range(T) :
    lst = []
    N = int(input())
    fibonacci(N, lst)
    print(lst.count(0), lst.count(1))'''

class FiboNum:
    def __init__(self):
        self.zero = -1
        self.one = 0

    def show(self):
        print(self.zero, self.one)

fibo = [FiboNum() for i in range(41)]
fibo[0].zero = 1
fibo[1].one = 1
fibo[1].zero = 0

for i in range(2, 41):
    if fibo[i].zero != -1:
        continue
    else:
        fibo[i].zero = fibo[i-1].zero + fibo[i-2].zero
        fibo[i].one = fibo[i - 1].one + fibo[i - 2].one

T = int(input())
for i in range(T):
    n = int(input())
    fibo[n].show()