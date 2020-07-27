def mergeSort(x) :
    if len(x) > 1 :

        # 분할 하는 부분
        mid = len(x) // 2
        lx, rx = x[:mid], x[mid:]
        mergeSort(lx)
        mergeSort(rx)

        # 병합하는 부분
        # left_index, right_index, 원래 배열의 인덱스 i
        li, ri, i = 0, 0, 0
        # 왼쪽, 오른쪽 쪼갠 부분을 둘중에 하나라도 끝까지 탐색하게 되면 while문을 탈출
        while li < len(lx) and ri < len(rx) :
            # lx리스트의 값이 rx리스트의 값보다 작다면
            if lx[li] < rx[ri] :
                # x 리스트에 작은 값부터 채워 넣는다 : 병합하는 부분
                x[i] = lx[li]
                # 그리고 lx리스트에서 맨앞부분(인덱스 li가 가리키는 부분)은 정렬을 마쳤으니
                # 값을 하나 늘려준다
                li += 1
            else :   # rx리스트의 값이 더 작다면 작은 것을 넣어준다
                x[i] = rx[ri]
                ri += 1
            # 졍렬을 원하는 x의 리스트도 위의 if~else문에서 값이 하나가 들어갔으니
            # 다음 인덱스에 정렬된 값을 넣기 위해서 i를 늘려준다
            i += 1
        # li != len(lx)  :  lx에 에 남은 값이 있다 = 남은 값은 가장 큰값
        # x[i:] = lx[li:]  :  while문 탈출 후에 rx혹은 lx에 남은 값들이 있다면
        # 위에서 while안에서 정렬을 하던 인덱스 i부터 이후에 남은 데이터 (lx나 rx에 남아있는 가장 큰값)
        # 를 if문을 통해서 lx, rx에 남은 값을 넣어준다
        x[i:] = lx[li:] if li != len(lx) else rx[ri:]

import sys

ipt = sys.stdin.readline
N = int(input())
lst = set()
#lst = []

for _ in range(N) :
    lst.add(int(ipt()))

#mergeSort(list(lst))

for j in sorted(lst) :
    print(j)