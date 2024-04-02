from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort()

heap = []

for start, end in lectures:
    heappush(heap, end)

    if heap[0] <= start:
        heappop(heap)

print(len(heap))
