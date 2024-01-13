# import heapq

INF = int(1e9)


# def solution(N, road, K):
#     graph = [[] for _ in range(N + 1)]
#     distance = [INF] * (N + 1)

#     for info in road:
#         a, b, c = info
#         graph[a].append((b, c))
#         graph[b].append((a, c))

#     q = []
#     heapq.heappush(q, (0, 1))
#     distance[1] = 0

#     while q:
#         dist, now = heapq.heappop(q)

#         if distance[now] < dist:
#             continue

#         for to, cost in graph[now]:
#             cost_total = dist + cost

#             if cost_total < distance[to]:
#                 distance[to] = cost_total
#                 heapq.heappush(q, (cost_total, to))

#     return len([dist for dist in distance if dist != INF and dist <= K])


def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]
    distance = [INF] * (N + 1)

    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    q = [(1, 0)]
    distance[1] = 0

    while q:
        now, dist = q.pop(0)

        for adj_node, adj_dist in graph[now]:
            cost = dist + adj_dist

            if cost < distance[adj_node]:
                distance[adj_node] = cost
                q.append((adj_node, cost))

    print(distance)            
    return len([dist for dist in distance if dist != INF and dist <= K])
