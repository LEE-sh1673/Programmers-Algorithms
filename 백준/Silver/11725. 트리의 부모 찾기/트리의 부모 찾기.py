from sys import stdin
from collections import defaultdict, deque

input = stdin.readline
n = int(input())
trees = defaultdict(list)
parents = [0] * (n+1)

def bfs(i):
    visited = [False] * (n+1)
    que = deque()
    
    que.append(i)
    visited[i] = True

    while que:
        node = que.popleft()

        for child in trees[node]:
            if not visited[child]:
                visited[child] = True
                parents[child] = node
                que.append(child)
    
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    trees[n1].append(n2)
    trees[n2].append(n1)

bfs(1)
print('\n'.join(map(str, parents[2:])))
