import sys
from collections import Counter

ipt = sys.stdin.readline

N = int(ipt())
#lst = set()
lst = []
hap = 0

for _ in range(N) :
    #lst.add(int(ipt()))
    lst.append(int(ipt()))

# 평균값
for i in lst :
    hap += i

avg = hap / len(lst)


# 중앙값
lst = sorted(lst)
mid = lst[len(lst)//2]


# 최빈값, counter사용
ll = []
cnt = Counter(lst)
cnt = sorted(cnt.items(), key = lambda x: x[1], reverse=True)
max_value = cnt[0][1]
for i in range(len(cnt)) :
    if cnt[i][1] == max_value :
        ll.append(cnt[i][0])
if len(ll) == 1 :
    cb = ll[0]
else :
    cb = ll[1]

# 범위
ran = lst[len(lst)-1] - lst[0]

print(int(round(avg, 0)))
print(mid)
print(cb)
print(ran)