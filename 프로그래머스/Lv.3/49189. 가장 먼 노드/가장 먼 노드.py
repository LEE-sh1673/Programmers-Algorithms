def solution(N, road):
    graph = [[] for _ in range(N + 1)]
    distances = [0] * (N + 1)
    visited = [False] * (N + 1)
    max_dist = 0

    for a, b in road:
        graph[a].append(b)
        graph[b].append(a)

    q = [1]
    visited[1] = True

    while q:
        node = q.pop(0)

        for adj_node in graph[node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                distances[adj_node] = distances[node] + 1
                q.append(adj_node)
    
    distances.sort(reverse=True)
    return distances.count(distances[0])
