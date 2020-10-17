import heapq

def heapsort(iterabale) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterabale:
        # 최대힙의 경우 value를 -value로 넣고
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소에 차례대로 꺼내어 담기
    for i in range(len(h)):
        # 최대힙의 경우 -heapq.heappop(h)로 꺼낸
        result.append(heapq.heappop(h))
    return result

if __name__ == '__main__':
    result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
    print(result)

    ## 혹은 다음과 같이 수행해도 min heap으로 수행됨
    a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    heapq.heapify(a)
    print(a)

    # 최대 힙
    a = list(map(lambda x: -x, a))
    heapq.heapify(a)
    a = list(map(lambda x: -x, a))
    print(a)