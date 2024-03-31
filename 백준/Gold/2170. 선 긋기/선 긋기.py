from sys import stdin

input = stdin.readline
n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
i = 0

temp = []

while i < n:
    x, y = lines[i]
    j = i

    while j < n-1 and y >= lines[j+1][0]:
        y = max(y, lines[j+1][1])
        j += 1

    temp.append([x, y])
    i = j + 1 if i != j else i + 1

print(sum([y-x for x, y in temp]))
