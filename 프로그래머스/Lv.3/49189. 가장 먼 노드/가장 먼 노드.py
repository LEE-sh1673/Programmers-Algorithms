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

    def dijkstra(start):
        nonlocal max_dist
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

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

    dijkstra(1)
    return len([dist for dist in distance if dist == max_dist])
