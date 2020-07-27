def convert_bin(a) :
    bin_num, count = "", 0

    bin_num = bin(a)
    bin_num = "".join(list(bin_num)[2:len(bin_num)])

    for a in bin_num :
        if a == "1" :
            count += 1

    return bin_num, count

def solution(n):
    answer = 0
    temp = 0
    origin_bin_n, origin_one_count = convert_bin(n)
    # print(bin_n, one_count)
    while True :
        if origin_one_count == temp :
            break

        n += 1
        _, temp = convert_bin(n)


    return n


if __name__ == "__main__" :
    n = 78
    # n = 15

    print(solution(n))

