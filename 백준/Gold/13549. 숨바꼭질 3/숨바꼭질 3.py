"""
13549. 숨바꼭질 3
"""
from collections import deque

MAX = 200000
check = [False] * MAX
dist = [-1] * MAX

n, m = map(int, input().split())
check[n] = True
dist[n] = 0

q = deque([n])
next_q = deque()

while q:
    now = q.popleft()

    if now * 2 < MAX and not check[now * 2]:
        q.append(now * 2)
        check[now * 2] = True
        dist[now * 2] = dist[now]

    for next_v in [now-1, now+1]:
        if MAX > next_v >= 0 and not check[next_v]:
            next_q.append(next_v)
            check[next_v] = True
            dist[next_v] = dist[now] + 1

    if not q:
        q = next_q
        next_q = deque()

print(dist[m])
