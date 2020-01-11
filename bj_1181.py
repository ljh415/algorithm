'''
N = int(input())
lst = set()

for _ in range(N) :
    lst.add(input())

lst = sorted(lst, key = len)

for i in lst :
    print(i)'''

import sys
from collections import defaultdict

#strings = sys.stdin.read().splitlines()
#strings = set(strings[1:])
N = int(input())
strings = set()

for _ in range(N) :
    strings.add(input())


dict_str = {}

for s in strings:
    dict_str[s] = len(s)

# 단어 길이 정렬
len_ordered_words = sorted(dict_str.items(), key=lambda x: x[1])

# 개수 별로 단어 묶기
dic_ordered_words = defaultdict(lambda: -1)

for w in len_ordered_words:
    if dic_ordered_words[w[1]] == -1:
        dic_ordered_words[w[1]] = [w[0]]
    else:
        dic_ordered_words[w[1]].append(w[0])

# 단어 사전 정렬
for l, w in dic_ordered_words.items():
    if len(w) > 1:
        dic_ordered_words[l] = sorted(w)

# 출력
for words in dic_ordered_words.values():
    for w in words:
        print(w)


# 출처 : https://roseline124.github.io/algorithm/2019/04/05/Altorithm-baekjoon-1181.html