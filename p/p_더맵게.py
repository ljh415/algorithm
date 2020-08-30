import heapq

def pre_solution(scoville, K):
    answer = 0
    a = 0
    count = 0
    heap = []

    # 힙생성
    for i in scoville:
        heapq.heappush(heap, i)
    # 최소힙구성, 가장 작은값을 먼저 a에 저장
    # 그 다음 작은 값에 2를 곱하여 다시 힙에 추가
    while heap[0] < K:
        a = heapq.heappop(heap)
        a += 2 * heapq.heappop(heap)
        heapq.heappush(heap, a)
        count += 1

    answer = count

    return answer


def solution(scoville, K):
    answer = 0
    a = 0
    count = 0
    heap = []
    # 힙생성
    for i in scoville:
        heapq.heappush(heap, i)
    # 최소힙구성, 가장 작은값을 먼저 a에 저장
    # 그 다음 작은 값에 2를 곱하여 다시 힙에 추가
    while heap[0] < K:
        try:
            a = heapq.heappop(heap)
            a += 2 * heapq.heappop(heap)
            heapq.heappush(heap, a)
        except:
            return -1

        count += 1

    answer = count

    return answer

if __name__ == '__main__':
    scoville, K = [1, 2, 3, 9, 10, 12], 7
    print(pre_solution(scoville, K))
    # print(solution(scoville, K))