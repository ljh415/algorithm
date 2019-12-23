han = 0

a = input()
int_a = int(a)


if (int_a < 100) :
    han = a
else :
    han = 99
    while int_a >= 100 :
        a = list(map(int, str(int_a)))
        #a_list = list(map(int, a))
        if a[2] - a[1] == a[1] - a[0] :
            han += 1

        int_a -= 1

print(type(han))