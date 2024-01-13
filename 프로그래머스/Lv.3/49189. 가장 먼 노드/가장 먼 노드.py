import heapq

INF = int(1e9)


def solution(N, road):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)
    max_dist = 0

    for info in road:
        a, b = info
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for to, cost in graph[now]:
            cost_total = dist + cost

            if cost_total < distance[to]:
                distance[to] = cost_total
                heapq.heappush(q, (cost_total, to))
                max_dist = max(max_dist, cost_total)

    return distance.count(max_dist)
