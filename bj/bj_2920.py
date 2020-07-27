umgae = [1, 2, 3, 4, 5, 6, 7, 8]
umgae_rev = list(reversed(umgae))
input_list = list(map(int, list(input().split(' '))))


if input_list == umgae :
    print("ascending")
elif input_list == umgae_rev :
    print("descending")
else :
    print("mixed")