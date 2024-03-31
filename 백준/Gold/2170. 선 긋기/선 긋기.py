from sys import stdin

input = stdin.readline
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

start, end = lines[0]
total = 0

for x, y in lines[1:]:
    if end >= x:
        end = max(end, y)
    else:
        total += end - start
        start, end = x, y

total += end - start
print(total)
