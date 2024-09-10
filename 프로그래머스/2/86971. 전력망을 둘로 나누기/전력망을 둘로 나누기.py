def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    def dfs(point, visited):
        cnt = 1
        visited[point] = True

        for v in graph[point]:
            if not visited[v]:
                cnt += dfs(v, visited)
        return cnt
    
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    answer = 1e10
    
    for v1, v2 in wires:
        # 임의의 전선을 끊는다.
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        visited = [False] * (n+1)
    
        # 임의의 지점에서부터 연결된 송전탑의 개수를 구한다.
        cnt = dfs(1, visited)
        
        # 두 전력망이 가진 송전탑 개수 차이(절대값)를 구한다.
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
        
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    return answer

    