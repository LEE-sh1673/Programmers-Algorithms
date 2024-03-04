"""
1697. 숨바꼭질
"""
from sys import stdin
from collections import deque


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = via[temp]
    print(' '.join(map(str, arr[::-1])))


def bfs():
    q = deque([N])

    while q:
        v = q.popleft()
        
        if v == K:
            print(dist[v])
            path(v)
            return v

        for next_v in (v + 1, v - 1, 2 * v):
            if 0 <= next_v <= 100000 and dist[next_v] == 0:
                dist[next_v] = dist[v] + 1
                via[next_v] = v
                q.append(next_v)


N, K = map(int, stdin.readline().split())
dist = [0] * 100001
via = [0] * 100001
bfs()
