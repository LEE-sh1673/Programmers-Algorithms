from sys import stdin
from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
heap = []

for num in map(int, input().split()):
    heappush(heap, num)

for _ in range(m):
    x = heappop(heap)
    y = heappop(heap)
    ret = x + y
    heappush(heap, ret)
    heappush(heap, ret)

print(sum(heap))
