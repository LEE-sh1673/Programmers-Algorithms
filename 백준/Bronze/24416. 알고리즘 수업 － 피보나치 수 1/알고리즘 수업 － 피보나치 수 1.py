from sys import stdin

n = int(stdin.readline())
a = 1
b = 2
for _ in range(3, n):
    a, b = b, a + b

print(b, n - 2)
