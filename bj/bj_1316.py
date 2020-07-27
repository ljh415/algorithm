case_num = int(input())
answer = []
for i in range(case_num):
    word = list(str(input()))

    for k in range(len(word)):
        if k != len(word) - 1 and word[k] == word[k + 1]:
            pass
        elif word[k + 1:].count(word[k]) != 0:
            break
        elif k == len(word) - 1:
            answer.append(i)

print(len(answer))

# 출처 : https://claude-u.tistory.com/44