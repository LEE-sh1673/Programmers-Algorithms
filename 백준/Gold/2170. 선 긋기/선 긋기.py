from sys import stdin

input = stdin.readline
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda line: line[0])

start, end = lines[0]
total = 0

for x, y in lines[1:]:
    if end < x:
        total += end - start
        start, end = x, y
    elif end < y:
        end = y

total += end - start
print(total)
