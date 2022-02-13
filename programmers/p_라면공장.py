def solution(stock, dates, supplies, k):
    import heapq

    answer = 0
    idx = 0
    q = []

    while stock < k:
        for i in range(idx, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(q, -supplies[i])
            # idx = i+1
        stock -= heapq.heappop(q)
        answer += 1

    return answer