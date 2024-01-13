import heapq

INF = int(1e9)


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for info in road:
        a, b, c = info
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
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

    dijkstra(1)
    return len([dist for dist in distance if dist != INF and dist <= K])