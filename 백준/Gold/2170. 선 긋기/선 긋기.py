from sys import stdin

input = stdin.readline
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort(key=lambda line: line[0])
start, end = lines[0]
total = 0

for i in range(1, n):
    x, y = lines[i]
    
    if end >= y:
        continue

    if end < x:
        total += end - start
        start, end = x, y
    else:
        end = y

total += end - start
print(total)
