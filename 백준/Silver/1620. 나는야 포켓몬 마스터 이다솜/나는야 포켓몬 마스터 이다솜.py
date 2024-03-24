from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
names = {i + 1: input().strip() for i in range(n)}
indexes = {value: key for key, value in names.items()}

for _ in range(m):
    target = input().strip()

    if target.isdigit():
        print(names[int(target)])
    else:
        print(indexes[target])
