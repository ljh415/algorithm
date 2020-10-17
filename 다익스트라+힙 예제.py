'''
도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나간다
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메세지를 받게 되는 도시의 개수는 총 몇 개이며
도시들이 모두 메세지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.
'''

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


dijkstra(start)

count = 0
max_distance = 0
for d in distance :
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count-1, max_distance)