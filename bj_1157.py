from collections import Counter

S = list(input().upper())

result = Counter(S)
Max = max(result.values())

if list(result.values()).count(Max) != 1 :
    print("?")
else :
    print(list(result.keys())[list(result.values()).index(Max)])
